import React from 'react';

const CONGRATULATIONS_ILLUSTRATION_LINK = window.location.protocol + '//' + window.location.host + '/static/frontend/images/pages/profile/congratulations/';

const SetupCongratulations: React.FC = () => {
  return (  
    <div className="max-w-lg mx-auto p-6 rounded">
      <h1 className="text-4xl font-bold text-center mb-10">Welcome To VividSync</h1>
      <div className="mb-4">
        <img src={CONGRATULATIONS_ILLUSTRATION_LINK + 'cont_crea_welcome.svg'} alt="Social Icon" className="" />
      </div>
      <div className='mb-4'>
        <p className="text-xl font-bold text-center mb-10">Congratulations, you are all set, Enjoy your journey to success 🙌 🎉</p>
      </div>
      <div className='mb-4'>
        <a href='/dashboard/' className="dark w-64 rounded-[10px]  bg-dark hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
          Start Journey
        </a>
      </div>
    </div>

  );
};

export default SetupCongratulations;
