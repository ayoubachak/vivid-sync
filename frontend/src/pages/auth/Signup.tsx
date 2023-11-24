// Signup.tsx
import { useForm, SubmitHandler } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';

type SignupFormInputs = {
    username: string;
    password: string;
};

const signupSchema = yup.object({
    username: yup.string().required('Username is required'),
    password: yup.string().min(4).required('Password is required'),
}).required();

export default function Signup() {
    const { register, handleSubmit, formState: { errors } } = useForm<SignupFormInputs>({
        resolver: yupResolver(signupSchema)
    });

    const onSubmit: SubmitHandler<SignupFormInputs> = data => {
        console.log(data);
        console.log("submitting login form..")
        // Call API to perform signup
    };

    return (
        <div className="flex justify-center items-center h-screen bg-gray-100">
            <div className="max-w-md w-full bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <h2 className="text-2xl font-bold mb-4 text-center">Join Us</h2>
                <p className="text-center mb-8">Create your account.</p>
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
                    <button className="w-full bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                        Signup
                    </button>
                </form>
            </div>
        </div>
    );
}
