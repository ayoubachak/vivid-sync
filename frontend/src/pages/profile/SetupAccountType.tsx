import React, { useState } from 'react';
import { AccountType } from '../../models/VividUser';


const SetupAccountType: React.FC = () => {
  const [selectedAccountType, setSelectedAccountType] = useState<AccountType | null>(null);

  const handleAccountTypeSelection = (account_type: AccountType) => {
    setSelectedAccountType(account_type);
  };

  return (
    <div>
      <h1>Choose account type</h1>
    </div>
  );
};

export default SetupAccountType;
