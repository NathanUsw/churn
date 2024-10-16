import numpy as np
import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()
Faker.seed(42)
np.random.seed(42)

# Number of records to generate
num_records = 10000

# Lists of possible values
genders = ['Male', 'Female', 'Other']
countries = ['USA', 'Canada', 'UK', 'Australia', 'Germany', 'France', 'India', 'Brazil', 'Japan', 'China']
occupations = ['Engineer', 'Teacher', 'Doctor', 'Lawyer', 'Artist', 'Manager', 'Clerk', 'Salesperson', 'Technician', 'Consultant']
subscription_types = ['Basic', 'Standard', 'Premium']
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cryptocurrency']
issues_reported = ['Login Issue', 'Payment Problem', 'Feature Request', 'Bug Report', 'Account Cancellation']
customer_satisfaction_ratings = [1, 2, 3, 4, 5]

# Generate data
data = []

for _ in range(num_records):
    # Customer Demographics
    age = np.random.randint(18, 70)
    gender = np.random.choice(genders)
    geographic_location = np.random.choice(countries)
    occupation = np.random.choice(occupations)
    
    # Account Information
    account_creation_date = fake.date_between(start_date='-5y', end_date='today')
    subscription_type = np.random.choice(subscription_types)
    contract_duration = np.random.choice([1, 6, 12, 24])  # in months
    renewal_status = np.random.choice(['Active', 'Pending', 'Expired'])
    
    # Service Usage Metrics
    login_frequency = np.random.poisson(lam=5)
    features_utilized = np.random.randint(1, 20)
    average_session_duration = round(np.random.uniform(5, 120), 2)  # in minutes
    time_since_last_login = np.random.randint(0, 60)  # in days
    
    # Customer Support Interactions
    support_tickets_filed = np.random.poisson(lam=1)
    if support_tickets_filed > 0:
        nature_of_issues_reported = np.random.choice(issues_reported, support_tickets_filed).tolist()
    else:
        nature_of_issues_reported = []
    resolution_time = round(np.random.uniform(1, 72), 2)  # in hours
    customer_satisfaction_rating = np.random.choice(customer_satisfaction_ratings)
    
    # Payment History
    payment_method = np.random.choice(payment_methods)
    on_time_payment_ratio = round(np.random.uniform(0.5, 1.0), 2)
    failed_transactions = np.random.poisson(lam=0.2)
    billing_cycle = np.random.choice(['Monthly', 'Quarterly', 'Yearly'])
    
    # Historical Churn Data
    past_churn = np.random.choice([0, 1], p=[0.8, 0.2])  # 20% chance of past churn
    if past_churn:
        time_since_last_churn = np.random.randint(1, 24)  # in months
        reengagement_attempts = np.random.randint(1, 5)
        reengagement_outcome = np.random.choice(['Successful', 'Unsuccessful'], p=[0.7, 0.3])
    else:
        time_since_last_churn = None
        reengagement_attempts = None
        reengagement_outcome = None
    
    # Current Churn Status (Target Variable)
    churn = np.random.choice([0, 1], p=[0.7, 0.3])  # 30% churn rate
    
    # Compile the record
    record = {
        # Customer Demographics
        'Age': age,
        'Gender': gender,
        'GeographicLocation': geographic_location,
        'Occupation': occupation,
        
        # Account Information
        'AccountCreationDate': account_creation_date,
        'SubscriptionType': subscription_type,
        'ContractDurationMonths': contract_duration,
        'RenewalStatus': renewal_status,
        
        # Service Usage Metrics
        'LoginFrequency': login_frequency,
        'FeaturesUtilized': features_utilized,
        'AverageSessionDurationMinutes': average_session_duration,
        'TimeSinceLastLoginDays': time_since_last_login,
        
        # Customer Support Interactions
        'SupportTicketsFiled': support_tickets_filed,
        'NatureOfIssuesReported': nature_of_issues_reported,
        'ResolutionTimeHours': resolution_time,
        'CustomerSatisfactionRating': customer_satisfaction_rating,
        
        # Payment History
        'PaymentMethod': payment_method,
        'OnTimePaymentRatio': on_time_payment_ratio,
        'FailedTransactions': failed_transactions,
        'BillingCycle': billing_cycle,
        
        # Historical Churn Data
        'PastChurn': past_churn,
        'TimeSinceLastChurnMonths': time_since_last_churn,
        'ReengagementAttempts': reengagement_attempts,
        'ReengagementOutcome': reengagement_outcome,
        
        # Target Variable
        'Churn': churn
    }
    
    data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Display first 5 records
print(df.head())

# Save to CSV
df.to_csv('synthetic_customer_data.csv', index=False)