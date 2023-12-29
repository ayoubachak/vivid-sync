import React, { useEffect, useState } from 'react';
import axiosInstance from '../../middleware/axiosMiddleware';
import { useNavigate, useParams } from 'react-router-dom';
import LoadingScreen from '../../components/LoadingScreen';

const PasswordReset: React.FC = () => {
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [isValidToken, setIsValidToken] = useState(false);
    const { uidb64, token } = useParams();
    const navigatge = useNavigate();
    console.log("uid", uidb64);
    console.log("token", token);
    useEffect(() => {
        // Validate uidb64 and token on component mount
        axiosInstance.get(`/api/registration/reset-password-confirm/${uidb64}/${token}`)
            .then(response => {
                setIsValidToken(true); // Set valid token state if response is successful
                console.log(response);
            })
            .catch(error => {
                console.error('Invalid token:', error);
               navigatge('/error'); 
            });
    }, [uidb64, token, history]);

    const handleResetPassword = async () => {
        if (password !== confirmPassword) {
            setErrorMessage("Passwords do not match.");
            return;
        }
    
        try {
            const response = await axiosInstance.post(`/api/registration/reset-password-confirm/${uidb64}/${token}/`, { password });
            console.log('Password reset successful:', response.data);
            // Redirect to login or other appropriate place after successful reset
            window.location.href = "/login/";
        } catch (error) {
            setErrorMessage('Password reset failed. Please try again.');
            console.error('Password reset failed:', error);
        }
    };

    if (!isValidToken) {
        return <LoadingScreen/>; // Or a loading spinner
    }

    return (
        <div className="light">
            <h1 className="text-6xl font-extrabold text-left mb-10">Reset Password</h1>
            <p>Please enter your new password:</p>
            
            <div className="reset-password-form">
                <label htmlFor="password" className="block text-gray-700 text-lg font-bold mb-2 text-left">
                    New Password
                </label>
                <input
                    type="password"
                    className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="password"
                    placeholder="Enter your new password..."
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <label htmlFor="confirmPassword" className="block text-gray-700 text-lg font-bold mb-2 text-left">
                    Confirm Password
                </label>
                <input
                    type="password"
                    className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="confirmPassword"
                    placeholder="Confirm your new password..."
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                />

                {errorMessage && <div>
                                <span className="text-red-500 text-xs italic">{errorMessage}</span>
                        </div>
                    }
                
                <button
                    onClick={handleResetPassword}
                    className="dark w-full md:w-64 rounded-[10px] bg-dark hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    Reset Password
                </button>
            </div>
        </div>
    );
};

export default PasswordReset;
