// ForgotPassword.tsx
import React, { useState } from 'react';
import axiosInstance from '../../middleware/axiosMiddleware';

const ForgotPassword: React.FC = () => {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handleForgotPassword = async () => {
        try {
            // Replace with your password reset request endpoint
            const response = await axiosInstance.post('/api/registration/reset-link/send/', { email });
            console.log('Reset password link sent:', response.data);
            setMessage('A password reset link has been sent to your email.');
        } catch (error) {
            setMessage('Failed to send reset password link. Please try again.');
            console.error('Failed to send reset password link:', error);
        }
    };

    return (
        <div className="light">
            <h1 className="text-6xl font-extrabold text-left mb-10">Forgot Password</h1>
            <p>Please enter your email to receive a password reset link:</p>
            
            <div className="forgot-password-form">
                <label htmlFor="email" className="block text-gray-700 text-lg font-bold mb-2 text-left">
                    Email
                </label>
                <input
                    type="email"
                    className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="email"
                    placeholder="Enter your email..."
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                {message && <span className={`text-${message.startsWith('Failed') ? 'red' : 'green'}-500 text-xs italic`}>{message}</span>}
                
                <button
                    onClick={handleForgotPassword}
                    className="dark w-full md:w-64 rounded-[10px] bg-dark hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    Send Reset Link
                </button>
            </div>
        </div>
    );
};

export default ForgotPassword;
