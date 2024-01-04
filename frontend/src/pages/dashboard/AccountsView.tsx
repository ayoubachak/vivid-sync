import  { useEffect, useState } from 'react';
import SocialMediaPlatform from '../../models/SocialMediaPlatform';
import DOMPurify from 'dompurify';
import { MEDIA_URL } from '../../services/links/links';
import axiosInstance from '../../middleware/axiosMiddleware';

const PLATFORMS_QUERY = `
  query {
    allSocialMediaPlatforms {
      name
      icon
      loginRedirectUrl
    }
  }
`;


const AccountsView = () => {
    const [platforms, setPlatforms] = useState<SocialMediaPlatform[]>([]);

    useEffect(() => {
      const fetchPlatforms = async () => {
          try {
              const response = await axiosInstance.post('/graphql/', {
                  query: PLATFORMS_QUERY
              });
              const platformsData = response.data.data.allSocialMediaPlatforms.map((platform : SocialMediaPlatform) => ({
                  ...platform,
                  loginRedirectUrl: DOMPurify.sanitize(platform.loginRedirectUrl),
                  icon: MEDIA_URL+ DOMPurify.sanitize(platform.icon)
                }));
              setPlatforms(platformsData);
          } catch (error) {
              console.error('Error fetching platforms:', error);
          }
      };
      fetchPlatforms();
  }, []);
  

    return (
        <div className="container mx-auto p-4">
            {platforms.map((platform : SocialMediaPlatform) => (
                <a 
                    key={platform.name}
                    href={platform.loginRedirectUrl}
                    className="flex items-center mb-4 p-2 border border-gray-300 rounded-lg hover:bg-gray-100"
                >
                    <img 
                        src={platform.icon} 
                        alt={platform.name} 
                        className="h-10 w-10 mr-2"
                    />
                    <span className="font-bold">{platform.name}</span>
                </a>
            ))}
        </div>
    );
};

export default AccountsView;
