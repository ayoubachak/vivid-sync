import React  from 'react'; 
import { AccountType } from '../../../models/VividUser';
import axiosInstance from '../../../middleware/axiosMiddleware';

const CHANGE_ACCOUNT_TYPE_MUTATION = `
  mutation ChangeAccountType($accountType: String!) {
    changeAccountType(accountType: $accountType) {
      user {
        id
        accountType
      }
      success
      message
    }
  }
`;

const AccountTypeCard = ({ accountType, image, onClick, isSelected }: { accountType: AccountType, image: string, onClick: (accountType: AccountType) => void, isSelected: boolean }) => {
  const description = {
    [AccountType.Influencer]: 'Lets you check all the inboxes, shows you trending post, displays analytics and helps you reach more people.',
    [AccountType.ContentCreator]: 'Helps you on your reach, helps you in creating content using AI, creates trendy videos and Blogs, lets you track the reach and manage.',
    [AccountType.Organization]: 'Work with your team, schedule posts, run ads, manage the team access and gathers all inboxes and business emails in one place, it also analyses the scam emails to prevent fraud.',
  };

  return (
    <div
      className={`flex-1 p-6 rounded-lg transition-shadow cursor-pointer ${isSelected ? 'ring-4 ring-text-color' : 'hover:shadow-lg'}`}
      onClick={() => onClick(accountType)}
    >
      <img src={image} alt={accountType} className="mx-auto mb-4 w-32 h-32" />
      <h2 className="text-2xl font-semibold mb-4">{accountType}</h2>
      <p>{description[accountType]}</p>
    </div>
  );
};



const SetupAccountType: React.FC = () => {
 
  const [accountType, setAccountType] = React.useState<AccountType | null>(null);
  
  const handleChoice = async () => {
    if (!accountType) {
      console.error('No account type selected');
      return;
    }

    try {
      const response = await axiosInstance.post('/graphql/', {
        query: CHANGE_ACCOUNT_TYPE_MUTATION,
        variables: {
          accountType: accountType,
        },
      });
      console.log('Account type changed:', response.data);
      if (response.data.data.changeAccountType.success) {
        window.location.href = '/me/';
      } else {
        throw new Error(response.data.data.changeAccountType.message);
      }
    } catch (error) {
      console.error('Error changing account type:', error);
    }
  };

  return (
    <>
    <main className="container light mx-auto my-10 p-8 rounded-lg text-center">
        <h1 className="text-4xl font-bold mb-10">Choose account type</h1>
        <div className="flex flex-col md:flex-row justify-center gap-10">
             {/* Influencer */}
            <AccountTypeCard 
              accountType={AccountType.Influencer} 
              image={window.location.origin + "/static/frontend/images/pages/profile/account type/influencer.png"} 
              onClick={setAccountType}
              isSelected={accountType === AccountType.Influencer}
            />
             {/* Content Creator */}
            <AccountTypeCard 
            accountType={AccountType.ContentCreator} 
            image={window.location.origin + "/static/frontend/images/pages/profile/account type/content_creator.png"} 
            onClick={setAccountType}
            isSelected={accountType === AccountType.ContentCreator}
            />
             {/* Organization */}
            <AccountTypeCard 
            accountType={AccountType.Organization} 
            image={window.location.origin + "/static/frontend/images/pages/profile/account type/organization.png"} 
            onClick={setAccountType}
            isSelected={accountType === AccountType.Organization}
            />
        </div>
        {/* when the user choses an account type, it should display a button Procede, and make the selected card glowing with a shadow to be clear what account type he chossed */}
        {accountType && <button 
        className="bg-text-color text-white font-bold px-6 py-2 rounded-[15px] hover:bg-color-secondary mt-10" 
        onClick={handleChoice}
        >Procede</button>}
    </main>
    
    </>
  );
};


export default SetupAccountType;
