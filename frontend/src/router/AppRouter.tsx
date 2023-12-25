// src/AppRouter.tsx
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Login from '../pages/auth/Login';
import Signup from '../pages/auth/Signup';
import Dashboard from '../pages/profile/Dashboard';
import VerifyEmail from '../pages/auth/VerifyEmail';
import TermsOfService from '../pages/auth/TermsOfService';
import SetupAccountType from '../pages/profile/setup/SetupAccountType';
import SetupPersonalInfo from '../pages/profile/setup/SetupPersonalInfo';

const PrivateRoute = ({ children }: { children: JSX.Element }) => {
    const { user } = useAuth();
    return user ? children : <Navigate to="/login" />;
};

const AppRouter = () => {
    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/signup/verify-email" element={<VerifyEmail />} />
                <Route path="/terms-of-service" element={<TermsOfService />} />
                <Route path="/complete-profile/account-type" element={<SetupAccountType />} />
                <Route path="/complete-profile/personal-info" element={<SetupPersonalInfo />} />
                <Route 
                    path="/dashboard" 
                    element={
                        <PrivateRoute>
                            <Dashboard />
                        </PrivateRoute>
                    } 
                />
            </Routes>
        </Router>
    );
};


export default AppRouter;
