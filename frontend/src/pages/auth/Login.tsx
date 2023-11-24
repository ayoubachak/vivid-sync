// Login.tsx
import { useForm, SubmitHandler } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import axiosInstance from '../../middleware/axiosMiddleware';
import { useNavigate } from 'react-router-dom';

type LoginFormInputs = {
    username: string;
    password: string;
};

const loginSchema = yup.object({
    username: yup.string().required('Username is required'),
    password: yup.string().min(4).required('Password is required'),
}).required();

export default function Login() {
    const navigate = useNavigate();
    const { register, handleSubmit, formState: { errors } } = useForm<LoginFormInputs>({
        resolver: yupResolver(loginSchema)
    });

    const onSubmit: SubmitHandler<LoginFormInputs> = async (data) => {
        try {
            console.log("submitting login form..")
            const response = await axiosInstance.post('/api/auth/token/', data);
            const { access_token, refresh_token } = response.data;
    
            // Store the tokens. For example, in localStorage (or consider a more secure storage)
            localStorage.setItem('accessToken', access_token);
            localStorage.setItem('refreshToken', refresh_token);
    
            // Redirect user or perform other actions upon successful login
            console.log('Login successful');
            navigate('/me');
        } catch (error) {
            console.error('Login failed', error);
            // Handle login failure (e.g., show an error message)
        }
    };

    return (
        <div className="flex justify-center items-center h-screen bg-gray-100">
            <div className="max-w-md w-full bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <h2 className="text-2xl font-bold mb-4 text-center">Welcome Back!</h2>
                <p className="text-center mb-8">Sign in to continue.</p>
                <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                    <div>
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
                            Username
                        </label>
                        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" {...register("username")} />
                        {errors.username && <span className="text-red-500 text-xs italic">{errors.username.message}</span>}
                    </div>
                    <div>
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                            Password
                        </label>
                        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" {...register("password")} />
                        {errors.password && <span className="text-red-500 text-xs italic">{errors.password.message}</span>}
                    </div>
                    <button className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                        Login
                    </button>
                </form>
            </div>
        </div>
    );
}
