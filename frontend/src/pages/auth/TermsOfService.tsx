import React from 'react';
import axiosInstance from '../../middleware/axiosMiddleware';

const TermsOfService: React.FC = () => {

    //  /api/users/terms-of-service/accept/
  const handleDecline =  () => {
        alert('You must accept the terms to use our service.');
    };

  const handleAccept = async () => {
    try {
        const response = await axiosInstance.post('/api/users/terms-of-service/accept/');
    
        if (response.status === 200) {
        console.log('Terms accepted successfully.');
        window.location.href = '/me/';
        } else {
        console.log('Failed to accept terms.');
        }
    } catch (error) {
        console.error('Error accepting terms:', error);
    }  
  };

  return (
    <>
        <h1 className="text-6xl font-extrabold text-center mb-10 text-custom-text">Terms of Service & Privacy Settings</h1>
        <main className="container mx-auto my-10 p-5 bg-white rounded-lg shadow-md border border-text-color">    
            <section className="mb-6">
                <h2 className="text-xl font-semibold">Terms of Service:</h2>
                <p className="mt-2 text-gray-600">
                    Just respect people and don't say nonsense man and you'll be good to go.
                    Keep in mind that we're a freemium service, which means some functionalities will be accessed after a subscription.
                </p>
            </section>

            <section className="mb-6">
                <h2 className="text-xl font-semibold">Privacy Settings:</h2>
                <p className="mt-2 text-gray-600">
                    We won't use any of your social media data except for knowing more about your audience to help increase your reach, the only data we'll use is the data you fill in the next forms, and it won't be shared with any third parties, we're not that cheap.
                </p>
            </section>

            <div className="flex justify-center">
                <button className="mx-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={handleAccept}>
                    Accept
                </button>
                <button className="mx-2 bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" onClick={handleDecline}>
                    Decline
                </button>
            </div>
        </main>
    </>
     
  );
};

export default TermsOfService;
