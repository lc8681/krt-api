# coding:utf-8

import os
import csv
import pandas as pda

csv_title = ['Personnel_category', 'job_number', 'employee_status', 'name', 'ID_number', 'birth_date', 'age',
             'ethnicity', 'gender', 'political_outlook', 'birthplace', 'marital_status', 'internship_category',
             'source_classification', 'department', 'department_full_name', 'entry_date', 'age_of_the_company_',
             'Working_time', 'length_of_service', 'job_sequence', 'job_hours', 'labor_contract_company',
             'labor_contract_start_date', 'labor_contract_termination_date',
             'number_of_labor_contracts_signed_after_2008', 'labor_contract_type', 'rank_category',
             'start_date_of_reemployment_agreement', 'Re_employment_agreement_termination_date',
             'internship_agreement_start_date', 'internship_agreement_termination_date', 'job_title', 'job_type',
             'job_title_name', 'job_title_level', 'skill_level', 'highest_education', 'highest_degree', 'major',
             'graduate_school', 'graduation_date', 'email_', 'Home_address_detailed', 'mobile_phone_number',
             'emergency_contact_name', 'emergency_contact_phone_number',
             'relationship_between_emergency_contact_and_himself', 'household_registration', 'physical_examination',
             'non_competition_agreement_identification', 'file_location', 'whether_the_file_is_in_the_company',
             'long_term_service_identification_', 'Address_on_ID_card', 'equity_incentive', 'shuttle_bus',
             'attendance_method', 'social_security_company', 'nature_of_account',
             'start_date_of_social_security_payment', 'insurance_payment_type', 'social_security_payment_period',
             'participating_pension_identification', 'participating_provident_fund_identification',
             'insurance_agency_company', 'provident_fund_personal_number', 'Social_security_base',
             'provident_fund_base', 'insurance_payment_place', 'salary_company', 'salary_attribution_department',
             'salary_first_level_department', 'salary_second_level_department', 'salary_third_level_department',
             'bank_name', 'account_bank_name', 'salary_account_number', 'participation_in_assessment', 'salary_package',
             'Breastfeeding_subsidy_start_date', 'breastfeeding_subsidy_end_date', 'overtime_deposit_mark',
             'overtime_hours_limit', 'comprehensive_working_hours_deposit_limit', 'resignation_category',
             'reason_for_resignation', 'last_working_day', 'advance_regularization_period_month', 'transaction_type',
             'trial_period_start_date', 'maternity_leave_start_Date', 'maternity_leave_end_date',
             'internship_transfer_date', 'probation_period_period_months', 'regularization_time',
             'original_rank_before_the_change', 'transaction_date', 'sector_name', 'second_level_department',
             'third_level_department', 'fourth_level_department', 'number_of_days_to_take_maternity_leave',
             'closed_Annual_leave', 'breastfeeding_subsidy_base', 'company_age_months', 'original_department',
             'original_job_title', 'part_time_information', 'recruitment_source', 'recruitment_type']
excel_path = 'excel_check/huamingce.xls'
csv_path = 'excel_check/huamingce.csv'


def excel_to_csv():
    try:
        os.remove(csv_path)
    except:
        pass
    with open(csv_path, 'a+', newline='', encoding='utf_8_sig')as f:
        f_csv = csv.writer(f, dialect='excel')
        f_csv.writerow(csv_title)
    ex = pda.read_excel(excel_path)
    ex.to_csv(csv_path, mode='a+', encoding="utf_8_sig", header=False, index=False, date_format='%Y-%m-%d')


if __name__ == '__main__':
    excel_to_csv()
