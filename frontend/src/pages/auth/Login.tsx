// Login.tsx
import { useForm, SubmitHandler } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import axiosInstance from '../../middleware/axiosMiddleware';
import {facebook_login,google_login, Facebook, Google } from '../../utils';
import { useState } from 'react';

type LoginFormInputs = {
    username: string;
    password: string;
};

const loginSchema = yup.object({
    username: yup.string().required('Username is required'),
    password: yup.string().min(4).required('Password is required'),
}).required();

export default function Login() {
    const [passwordShown, setPasswordShown] = useState(false);
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
            window.location.href = '/me/';
        } catch (error) {
            console.error('Login failed', error);
            // Handle login failure (e.g., show an error message)
        }
    };
 
    
    const togglePasswordVisibility = () => {
        setPasswordShown(!passwordShown);
    };


    return (<>
        <div className='light'>

            <h1 className="text-6xl font-extrabold text-left mb-10">Log In</h1>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                {/* Email Input */}
                <div>
                    <label className="block text-gray-700 text-lg font-bold mb-2 text-left" htmlFor="username">
                        Email
                    </label>
                    <input className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border border-gray-300 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="username" placeholder="Ex: example@example.com" {...register("username")} />
                    {errors.username && <span className="text-red-500 text-xs italic">{errors.username.message}</span>}
                </div>
                {/* Password Input */}
                <div>
                    <label className="block text-gray-700 text-lg font-bold mb-2 text-left" htmlFor="username">
                        Create Password
                    </label>
                    <div className='flex'>
                        <input
                            className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                            id="password"
                            type={passwordShown ? "text" : "password"}
                            placeholder="Create your new password..."
                            {...register("password")}
                        />
                        <button onClick={togglePasswordVisibility} type="button" className=' ml-5'>
                            {passwordShown ? "Hide" : "Show"}
                        </button>
                    </div>
                    {errors.password && <span className="text-red-500 text-xs italic">{errors.password.message}</span>}
                </div>
                {/* Log In Button */}
                <button className="dark w-64 rounded-[10px]  bg-dark hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                    Log In
                </button>
                {/* Forgot Password Link */}
                <div className="text-center">
                    <a href="/forgot-password/" className="font-bold" style={{ textDecoration: 'underline', color:"#E36B4B" }}>
                        Forgot Password?
                    </a>
                </div>
                {/* Divider */}
                <div className="relative flex py-5 items-center">
                    <div className="flex-grow" style={{ borderTop: '2px solid #E36B4B' }}></div>
                    <span className="flex-shrink mx-4 text-gray-600 font-bold">Or</span>
                    <div className="flex-grow" style={{ borderTop: '2px solid #E36B4B' }}></div>
                </div>

                {/* Google and Facebook Login Options */}
                <div className="flex flex-col space-y-4">
                    {/* Google Login Button */}
                    <button 
                        onClick={google_login}
                        type='button' 
                        className="font-bold h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline flex items-center justify-center">
                        <img src={Google} width={33} height={33} alt="Google" className="mr-2" /> Login with Google
                    </button>

                    {/* Facebook Login Button */}
                    <button 
                        onClick={facebook_login}
                        type='button' 
                        className="font-bold h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline flex items-center justify-center">
                        <img src={Facebook} width={33} height={33} alt="Facebook" className="mr-2" /> Login with Facebook
                    </button>
                </div>
                {/* Bottom Splitter */}
                <div className="flex-grow" style={{ borderTop: '2px solid #E36B4B' }}></div>
                {/* Sign Up Suggestion */}
                <div className="text-center font-bold">
                    <span className="text-gray-700">Don't have an Account?</span>{' '}
                    <a href="/signup/" style={{ textDecoration: 'underline', color:"#E36B4B"}}>
                        Sign Up here
                    </a>
                </div>
            </form>
        </div>
    </>
    );
}
