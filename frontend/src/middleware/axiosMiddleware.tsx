import axios from 'axios';

function getCookie(name : string) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
        'X-CSRFToken': csrftoken, // this is important for the hybrid approach between django and react
    },
});

// Request interceptor to attach token
axiosInstance.interceptors.request.use(config => {
    const accessToken = localStorage.getItem('accessToken');
    if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`;
    }
    return config;
}, error => {
    return Promise.reject(error);
});

// Response interceptor to refresh token
axiosInstance.interceptors.response.use(response => {
    return response;
}, async error => {
    // Check if 'error.response' exists before accessing 'status'
    if (error.response && error.response.status === 401 && !error.config._retry) {
        error.config._retry = true;
        const refreshToken = localStorage.getItem('refreshToken');

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/auth/token/refresh/', { refresh_token: refreshToken });
            localStorage.setItem('accessToken', response.data.access_token);
            axiosInstance.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access_token;
            return axiosInstance(error.config);
        } catch (refreshError) {
            // Handle refresh token failure (e.g., redirect to login, clear storage)
            return Promise.reject(refreshError);
        }
    }
    return Promise.reject(error);
});

export default axiosInstance;
