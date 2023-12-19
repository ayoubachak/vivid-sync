// Signup.tsx
import { useForm, SubmitHandler } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import {facebook_login,google_login, Facebook, Google } from '../../utils';
import { useState } from 'react';

type SignupFormInputs = {
    firstName: string;
    lastName: string;
    email: string;
    password: string;
};

const signupSchema = yup.object({
    firstName: yup.string().required('First Name is required'),
    lastName: yup.string().required('Last Name is required'),
    email: yup.string().email('Email is invalid').required('Email is required'),
    password: yup.string().min(4).required('Password is required'),
}).required();

export default function Signup() {
    const [passwordShown, setPasswordShown] = useState(false);
    const { register, handleSubmit, formState: { errors } } = useForm<SignupFormInputs>({
        resolver: yupResolver(signupSchema)
    });

    const onSubmit: SubmitHandler<SignupFormInputs> = data => {
        console.log(data);
        console.log("submitting signup form..")
        // Call API to perform signup
    };
    const togglePasswordVisibility = () => {
        setPasswordShown(!passwordShown);
    };
    
    return (
        <div className="light">
            <h1 className="text-6xl font-extrabold text-left mb-10">Sign Up</h1>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                {/* Flex container for first name and last name */}
                <div className="flex flex-wrap -mx-3 mb-6">
                    {/* First Name */}
                    <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                        <label className="block text-gray-700 text-lg font-bold mb-2 text-left" htmlFor="firstName">
                            First Name
                        </label>
                        <input className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="firstName" type="text" placeholder="Ex: John" {...register("firstName")} />
                        {errors.firstName && <span className="text-red-500 text-xs italic">{errors.firstName.message}</span>}
                    </div>
                    {/* Last Name */}
                    <div className="w-full md:w-1/2 px-3">
                        <label className="block text-gray-700 text-lg font-bold mb-2 text-left" htmlFor="lastName">
                            Last Name
                        </label>
                        <input className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="lastName" type="text" placeholder="Ex: Doe" {...register("lastName")} />
                        {errors.lastName && <span className="text-red-500 text-xs italic">{errors.lastName.message}</span>}
                    </div>
                </div>
                {/* Email */}
                <div>
                    <label className="block text-gray-700 text-lg font-bold mb-2 text-left" htmlFor="email">
                        Email
                    </label>
                    <input className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" placeholder="Ex: example@example.com" {...register("email")} />
                    {errors.email && <span className="text-red-500 text-xs italic">{errors.email.message}</span>}
                </div>
                {/* Password */}
                <div> 
                    <label className="block text-gray-700 text-lg font-bold mb-2 text-left" htmlFor="password">
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
                {/* Submit Button */}
                <button className="dark w-full md:w-64 rounded-[10px] bg-dark hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                    Sign Up
                </button>
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
                        <img src={Google} width={33} height={33} alt="Google" className="mr-2" /> Signup with Google
                    </button>

                    {/* Facebook Login Button */}
                    <button 
                        onClick={facebook_login}
                        type='button' 
                        className="font-bold h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline flex items-center justify-center">
                        <img src={Facebook} width={33} height={33} alt="Facebook" className="mr-2" /> Signup with Facebook
                    </button>
                </div>
                {/* Bottom Splitter */}
                <div className="flex-grow" style={{ borderTop: '2px solid #E36B4B' }}></div>
                {/* Sign Up Suggestion */}
                <div className="text-center font-bold">
                    <span className="text-gray-700">Already have an Account?</span>{' '}
                    <a href="/login/" style={{ textDecoration: 'underline', color:"#E36B4B"}}>
                        Login here
                    </a>
                </div>
            </form>

        </div>
    );
}
