import React, { useState } from 'react';
import axiosInstance from '../../../middleware/axiosMiddleware';
import { debounce } from 'lodash';

// Define a Gender type
type Gender = 'male' | 'female';

const SetupPersonalInfo: React.FC = () => {
    const [gender, setGender] = useState<Gender>('male');
    const [profilePic, setProfilePic] = useState<string>('');
    const [isUploading, setIsUploading] = useState<boolean>(false);
    const [uploadError, setUploadError] = useState("");
    const [usernameAvailability, setUsernameAvailability] = useState("");


    const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault();
      console.log('Form submitted');
    };

    const handleGenderChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      setGender(e.target.value as Gender);
    };

    const handleProfilePicChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
        const files = e.target.files;
        if (files && files.length > 0) {
            const file = files[0];

            // Reset previous error
            setUploadError("");

            // Check file size (2 MB limit)
            if (file.size > 2 * 1024 * 1024) {
                setUploadError("File size exceeds 2 MB.");
                return;
            }

            setIsUploading(true);
            const formData = new FormData();
            formData.append('profile_picture', file);

            try {
                const response = await axiosInstance.post('/api/users/profile-picture/upload/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });
                setProfilePic(response.data.profile_picture_url);
            } catch (error) {
                console.error('Error uploading the file', error);
                setUploadError("An error occurred while uploading the file.");
            } finally {
                setIsUploading(false);
            }
        }
    };

    const handleDeletePic = async () => {
        setIsUploading(true);
        try {
            await axiosInstance.delete('/api/users/profile-picture/delete/'); // Assuming this is your API endpoint
            setProfilePic('');
        } catch (error) {
            console.error('Error deleting the file', error);
        } finally {
            setIsUploading(false);
        }
    };

    const getProfilePicSrc = () => {
      if (profilePic) return profilePic;
      return gender === 'male'
        ? window.location.origin + "/static/frontend/images/pages/profile/avatars/male.svg"
        : window.location.origin + "/static/frontend/images/pages/profile/avatars/female.svg";
    };
    
    const checkUsernameAvailability = debounce(async (username) => {
        try {
            // Replace with the actual API call
            const response = await axiosInstance.get(`/api/users/check/username/${username}/`);
            setUsernameAvailability(response.data.message);
        } catch (error) {
            console.error('Error checking username availability', error);
            setUsernameAvailability("Error checking username availability.");
        }
    }, 500);  
    const handleUsernameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const username = e.target.value;
        // Regular expression for valid usernames
        const validUsernameRegex = /^[a-zA-Z0-9._]+$/;
    
        // Reset previous availability message
        setUsernameAvailability("");
    
        // Check if the username only contains valid characters
        if (!validUsernameRegex.test(username)) {
            setUsernameAvailability("Username contains invalid characters.");
            return; // Stop further execution if invalid
        }
    
        // If valid, check availability from backend
        checkUsernameAvailability(username);
    };
    

    return (
      <main className="container mx-auto my-10 p-8 rounded-lg">
        <h1 className="text-4xl font-bold text-center mb-10">Complete Profile Setup</h1>
        <form onSubmit={handleSubmit} className="md:flex md:space-y-0 space-y-6">
            <section className="flex flex-col items-center w-full md:w-1/2 md:border-r-2 md:pr-4">
            <h2 className="text-lg font-semibold mb-4">Insert your profile Picture</h2>
            <div className="border-text-color border-2 rounded-full mb-4 overflow-hidden w-24 h-24 md:w-48 md:h-48 flex justify-center items-center">
              <label htmlFor="profilePicUpload" className="cursor-pointer">
                <img
                  src={getProfilePicSrc()}
                  alt="Profile Placeholder"
                  className="inline-block object-cover rounded-full"
                />
                <input id="profilePicUpload" type="file" className="hidden" onChange={handleProfilePicChange} />
              </label>
            </div>
            <div className="text-red-500">{uploadError}</div>
            {/* Action buttons on the profile pic */}
            <div className="flex justify-center space-x-2 mt-4">
                <label className="bg-white hover:bg-slate-50 border-2 border-text-color text-white font-bold p-2 rounded-full flex items-center justify-center cursor-pointer">
                    <img
                    src={window.location.origin + "/static/frontend/images/icons/actions/edit.svg"}
                    alt="Edit"
                    className="w-6 h-6"
                    />
                    <input type="file" className="hidden" onChange={handleProfilePicChange} />
                </label>
                <button
                    type="button"
                    className="bg-white hover:bg-slate-50 border-2 border-text-color text-white font-bold p-2 rounded-full flex items-center justify-center"
                    onClick={handleDeletePic}
                >
                    <img
                    src={window.location.origin + "/static/frontend/images/icons/actions/delete.svg"}
                    alt="Delete"
                    className="w-6 h-6"
                    />
                </button>
            </div>
            <div className="relative">
                {/* Loading bar */}
                {isUploading && (
                <div className="absolute bottom-0 left-0 right-0 bg-blue-600 h-1"></div>
                )}
            </div>
            {/* Gender selection section */}
            <div className="flex justify-center gap-4 mt-4">
            {['male', 'female'].map((g) => (
                <label key={g} className="flex items-center cursor-pointer">
                <input
                    type="radio"
                    className="sr-only"
                    name="gender"
                    value={g}
                    checked={gender === g}
                    onChange={handleGenderChange}
                />
                <div className={`border-2 p-2 rounded-full ${gender === g ? 'bg-text-color border-text-color' : 'bg-white border-gray-300'} transition duration-300 ease-in-out`}>
                    <span className={`text-sm ${gender === g ? 'text-white' : 'text-gray-500'}`}>{g.charAt(0).toUpperCase() + g.slice(1)}</span>
                </div>
                </label>
            ))}
            </div>
            </section>

            <section className="md:w-1/2 w-full md:pl-4">
                <div className="mb-4 ">
                    <label htmlFor="username" className="block text-2xl text-sm font-bold mb-2 text-left">
                        What's your username in social media platforms*
                    </label>
                    <input
                        type="text"
                        id="username"
                        placeholder="@gorlockthedestroyer"
                        className="sh-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                        onChange={handleUsernameChange}
                        required
                    />
                    <div className="text-sm text-gray-600">{usernameAvailability}</div>
                </div>
                <div className="mb-4">
                    <label htmlFor="bio" className="block text-2xl text-sm font-bold mb-2 text-left">
                    Write a Bio that describes you
                    </label>
                    <textarea
                    id="bio"
                    placeholder="Some words that describe you..."
                    className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    required
                    />
                </div>
                <div className="mb-4">
                    <label htmlFor="hashtags" className="block text-2xl text-sm font-bold mb-2 text-left">
                    Some Hashtags you are interested in:
                    </label>
                    <input
                        type="text"
                        id="hashtags"
                        placeholder="#travel, #france, #fyp"
                        className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    />
                </div>
            </section>
      </form>
    </main>
  );
};

export default SetupPersonalInfo;
