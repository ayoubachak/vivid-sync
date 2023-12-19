import React, { useState } from 'react';
import { UseFormRegister, FieldValues, FieldErrors } from 'react-hook-form';

type PasswordInputProps = {
    register: UseFormRegister<FieldValues>;
    fieldName: string;
    errors: FieldErrors;
};

const PasswordInput: React.FC<PasswordInputProps> = ({ register, fieldName, errors }) => {
    const [passwordShown, setPasswordShown] = useState(false);

    const togglePasswordVisibility = () => {
        setPasswordShown(!passwordShown);
    };

    // Check if error message is a string before rendering
    const errorMessage = errors[fieldName]?.message;
    const isError = typeof errorMessage === 'string' && errorMessage.length > 0;

    return (
        <div>
            <input
                className="password-input"
                type={passwordShown ? "text" : "password"}
                {...register(fieldName)}
            />
            <button onClick={togglePasswordVisibility} type="button">
                {passwordShown ? "Hide" : "Show"}
            </button>
            {isError && <span className="error">{errorMessage}</span>}
        </div>
    );
};

export default PasswordInput;
