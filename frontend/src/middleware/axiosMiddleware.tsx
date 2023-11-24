import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
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
