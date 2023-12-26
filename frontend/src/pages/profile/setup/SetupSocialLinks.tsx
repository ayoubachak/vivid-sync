import  { useEffect, useState } from 'react';
import axiosInstance from '../../../middleware/axiosMiddleware';

const SOCIAL_ICONS_URL = window.location.protocol + '//' + window.location.host + '/static/frontend/images/icons/social/';

const SetupSocialLinks = () => {
  const [website, setWebsite] = useState('');
  const [instagram, setInstagram] = useState('');
  const [facebook, setFacebook] = useState('');
  const [youtube, setYoutube] = useState('');
  const [twitter, setTwitter] = useState('');
  const [linkedin, setLinkedin] = useState('');

const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Process the data
    console.log(website, instagram, facebook, youtube, twitter, linkedin);
    // Redirect or update state accordingly
    const socialLinksData = {
        links: [
          { type: 'website', url: website },
          { type: 'instagram', url: instagram },
          { type: 'facebook', url: facebook },
          { type: 'youtube', url: youtube },
          { type: 'twitter', url: twitter },
          { type: 'linkedin', url: linkedin }
        ].filter(link => link.url) // This will ensure only links with URLs are sent
      };

      try {
        // Send a POST request to the endpoint responsible for handling social links
        const response = await axiosInstance.post('/api/social/social-links/update/', socialLinksData);
        
        if (response.status === 200) {
          // If the response is successful, redirect to the congratulations page
          window.location.href = '/complete-profile/congratulations/';
        } else {
          // Handle any other HTTP responses
          console.error('Error updating social links:', response.statusText);
        }
      } catch (error : any) {
        // Handle errors with the request itself (e.g., network errors)
        console.error('Error during social links update:', error.message);
      }
  };

  const handleSkip = () => {
  
    window.location.href = '/complete-profile/congratulations/';
};

    useEffect(() => {
        const fetchSocialLinks = async () => {
        try {
            // Replace with the actual API endpoint to get the user's social links
            const response = await axiosInstance.get('/api/social/social-links/get/');
            const data = response.data;

            // Update state with the fetched data
            setWebsite(data.website || '');
            setInstagram(data.instagram || '');
            setFacebook(data.facebook || '');
            setYoutube(data.youtube || '');
            setTwitter(data.twitter || '');
            setLinkedin(data.linkedin || '');
        } catch (error) {
            console.error('Error fetching social links:', error);
            // Handle error appropriately
        }
        };

        fetchSocialLinks();
    }, []);

  return (
    <div className="max-w-lg mx-auto p-6 rounded">
      <h1 className="text-4xl font-bold text-center mb-10">Last Steps</h1>
      <p className="text-gray-700 mb-4">You can always add or change them later</p>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="website" className="block text-2xl font-bold mb-2 ">
            Website
          </label>
          <input
            type="text"
            id="website"
            placeholder="Ex: www.example.com"
            value={website}
            onChange={(e) => setWebsite(e.target.value)}
            className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border border-gray-300 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        {/* Repeat for each social media input */}
        <SocialLinkInput
          iconPath={SOCIAL_ICONS_URL + "instagram.svg"} // Replace with actual path to icon
          placeholder="Ex: https://instagram.com/your_username"
          value={instagram}
          onChange={setInstagram}
        />

        <SocialLinkInput
          iconPath={SOCIAL_ICONS_URL + "facebook.svg"}
          placeholder="Ex: https://facebook.com/your_username"
          value={facebook}
          onChange={setFacebook}
        />

        <SocialLinkInput
          iconPath={SOCIAL_ICONS_URL + "youtube.svg"}
          placeholder="Ex: https://youtube.com/your_username"
          value={youtube}
          onChange={setYoutube}
        />

        <SocialLinkInput
          iconPath={SOCIAL_ICONS_URL + "x.svg"}
          placeholder="Ex: https://twitter.com/your_username"
          value={twitter}
          onChange={setTwitter}
        />

        <SocialLinkInput
          iconPath={SOCIAL_ICONS_URL + "linkedin.svg"}
          placeholder="Ex: https://linkedin.com/in/your_username"
          value={linkedin}
          onChange={setLinkedin}
        />

        <div className="flex justify-between items-center mt-6">
          <button
            type="submit"
            className="dark w-64 rounded-[10px]  bg-dark hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Continue
          </button>
          <button
            type="button"
            className="underline hover:text-gray-500 text-center text-slate-700 text-[24px] font-bold"
            onClick={handleSkip}
          >
            Skip
          </button>
        </div>
      </form>
    </div>
  );
};

const SocialLinkInput = ({ iconPath, placeholder, value, onChange }: { iconPath: string, placeholder: string, value: string, onChange: (value: string) => void }) => (
  <div className="mb-4 flex items-center">
    <img src={iconPath} alt="Social Icon" className="h-12 w-12 mr-3" />
    <input
      type="text"
      placeholder={placeholder}
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border border-gray-300 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
    />
  </div>
);

export default SetupSocialLinks;
