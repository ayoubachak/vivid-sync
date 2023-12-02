import { useForm } from "react-hook-form";

interface FormInputProps {
    label: string;
    id: string;
    type: string;
    placeholder: string;
    register: ReturnType<typeof useForm>['register'];
    errorMessage?: string;
}


export const FormInput: React.FC<FormInputProps> = ({ label, id, type, placeholder, register, errorMessage }) => {
    return (
        <div>
            <label className="block text-gray-700 text-lg font-bold mb-2 text-left" htmlFor={id}>
                {label}
            </label>
            <input
                className="h-[48px] bg-white rounded-[10px] border-2 border-slate-700 shadow appearance-none border border-gray-300 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id={id}
                type={type}
                placeholder={placeholder}
                {...register(id)}
            />
            {errorMessage && <span className="text-red-500 text-xs italic">{errorMessage}</span>}
        </div>
    );
};
