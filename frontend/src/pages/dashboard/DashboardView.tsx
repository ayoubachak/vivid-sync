import React, {  useEffect, useState } from 'react';

const DashboardView: React.FC = () => {
  const [accounts, setAccounts ] = useState([]);

  useEffect(()=>{
    setAccounts([]);
  },[])


  return (
    <>
      <div className="mb-4">
        <h1 className="text-2xl font-semibold text-gray-900 text-text-color">Home</h1>
        <p className="text-gray-600">Welcome back Gorlock 👋, Here is the recap!</p>
      </div>
      <div className='flex flex-col justify-center items-center p-4'>
        {accounts.length === 0 ? (
            <div className="flex flex-col justify-center items-center">
            <div className='mb-4'>
              <p className="text-gray-600">You haven't connected any social media platforms yet, to do so go to the accounts tab and hook up your account or click the botton bellow</p>
            </div>
            <div>
              <a
              href='/accounts/' 
              className="dark w-64 rounded-[10px]  bg-dark hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                Connect an Account
              </a>
            </div>
          </div>
        ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            </div>
        )
        }
      </div>

    </>
  );
};

export default DashboardView;
