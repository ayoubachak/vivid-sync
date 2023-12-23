import React, { useEffect, useState } from 'react';
import axiosInstance from '../../middleware/axiosMiddleware';

const VerifyEmail: React.FC = () => {
    const [code, setCode] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [email, setEmail] = useState('');


    const handleVerify = async () => {
        try {
            // Replace '/api/verify-email/' with the correct endpoint
            const response = await axiosInstance.post('/api/registration/verify-email/check/', { code });
            console.log('Verification successful:', response.data);
            // Redirect to profile or other appropriate place after successful verification
            window.location.href = '/me/';
        } catch (error) {
            // Handle errors here, such as displaying a message to the user
            setErrorMessage('Verification failed. Please try again.');
            console.error('Verification failed:', error);
        }
    };

    const handleResendCode = async () => {
        try {
            // Replace '/api/resend-code/' with the correct endpoint
            // This endpoint should be a GET request as per the backend implementation
            const response = await axiosInstance.get('/api/registration/verify-email/resend/');
            console.log('Resend successful:', response.data);
            setErrorMessage('A new code has been sent to your email.');
        } catch (error) {
            // Handle errors here, such as displaying a message to the user
            setErrorMessage('Failed to resend code. Please try again.');
            console.error('Failed to resend code:', error);
        }
    };
    
    useEffect(() => {
        const fetchEmail = async () => {
            try {
              const query = `
                query {
                  me {
                    email
                  }
                }
              `;
          
              const graphqlResponse = await axiosInstance.post('/graphql/', {
                query: query
              });
              
              const { data } = graphqlResponse.data; // Adjust this line based on how the data is structured in your response
              if (data && data.me && data.me.email) {
                setEmail(maskEmail(data.me.email)); // Update the state with the masked email
              }
            } catch (error) {
              console.error('Error fetching email via GraphQL:', error);
              // Optionally set an error state here
            }
        };
          

        fetchEmail();
    }, []);
    const maskEmail = (email : string) => {
        const [user, domain] = email.split('@');
        const maskedUser = user.substring(0, 1) + user.substring(1).replace(/./g, '*');
        return `${maskedUser}@${domain}`;
    };
    return (
        <div className="light">
            <h1 className="text-6xl font-extrabold text-left mb-10">Verify Email</h1>
            <p>We’ve sent you an Email Containing a 6 digit Code, Please check your Inbox at:</p>
            <p className="masked-email">{email || 'Loading...'}</p>
            
            <div className="verification-form">
                <label htmlFor="code" className="block text-gray-700 text-lg font-bold mb-2 text-left">
                    Code
                </label>
                <input
                    type="text"
                    className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="code"
                    placeholder="Enter the 6 Digit Code..."
                    value={code}
                    onChange={(e) => setCode(e.target.value)}
                />
                {errorMessage && <span className="text-red-500 text-xs italic">{errorMessage}</span>}
                
                <button
                    onClick={handleVerify}
                    className="dark w-full md:w-64 rounded-[10px] bg-dark hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    Verify
                </button>

                <p className="resend">
                    If you did not receive the Email, <button onClick={handleResendCode} className="text-blue-600 hover:text-blue-800">Resend the Code</button> or <a href="/change-email" className="text-blue-600 hover:text-blue-800">Change Email</a>
                </p>
            </div>
        </div>
    );
};

export default VerifyEmail;
