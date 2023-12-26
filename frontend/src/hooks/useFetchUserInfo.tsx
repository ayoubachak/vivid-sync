import { useEffect, useState } from "react";
import { VividUser } from "../models/VividUser";
import axiosInstance from "../middleware/axiosMiddleware";

const GET_USER_INFO_QUERY = `
  query {
    me {
      id
      username
      email
      gender
      profilePicture
      bio
    }
  }
`;


export function useFetchUserInfo() {
    const [user, setUser] = useState<VividUser | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
  
    useEffect(() => {
      const fetchUserInfo = async () => {
        try {
          // Make a POST request with your GraphQL query
          const response = await axiosInstance.post('/graphql/', { query: GET_USER_INFO_QUERY });
          // If your Axios instance does not throw an error for non-2xx status codes,
          // you should check response.status here and throw an error if it's not 2xx
          setUser(response.data.data.me); // Assuming your GraphQL API returns the data under 'data.me'
        } catch (err) {
          setError('An error occurred while fetching user information.');
          // You might want to log the error or handle it based on its structure
          // console.error(err);
        } finally {
          setLoading(false);
        }
      };
  
      fetchUserInfo();
    }, []); // Empty dependency array means this effect runs once on mount
  
    return { user, loading, error };
  }