import React, { createContext, useContext, useState, ReactNode, useEffect } from 'react';
import axiosInstance from '../middleware/axiosMiddleware';
import { VividUser } from '../models/VividUser';

type AuthContextType = {
    user: VividUser | null; 
    loading: boolean;
    login: (user: any) => void; 
    logout: () => void;
};

const AuthContext = createContext<AuthContextType>(null!);

export const useAuth = () => useContext(AuthContext);

interface AuthProviderProps {
    children: ReactNode; // Explicitly type 'children'
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
    const [user , setUser] = useState<VividUser | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        axiosInstance.get('/api/users/me/info/')
        .then(response => {
            setUser(response.data);
            setLoading(false);
        })
        .catch(() => {
            setUser(null);
            setLoading(false);
        });
    }, []);

    const login = (userData: any) => {
        // Replace 'any' with your user type
        localStorage.setItem('accessToken', userData.access_token);
        localStorage.setItem('refreshToken', userData.refresh_token);
        setUser(userData.user);
    };

    const logout = () => {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        setUser(null);
    };
    

    return (
        <AuthContext.Provider value={{ user, loading, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
