import streamlit as st
st.markdown(""" This page basically defines the parameters values that has to be used in 
the student dropout prediction machine learning model -
1. Martial_Status - dtype = Integer,
Description - 1 - single , 2 - married , 3 - widower, 4- divorced, 5- factounion , 6 - legally separated

2. Application_mode - dtype = Integer,
Description - 1 - 1st phase general contingent , 2 -1st phase special contigent(Azores Island),
7 - Holders of other higher courses , 10 - International student(bachelor), 16 - 1st phase contigent(Madeira Island),
17 - 2nd phase general contigent, 18 - 3rd phase general contigent,26 - item b2 , 27 - other institution,39- over 23
years , 42 - Transfer, 43 - Change of course, 44 - Technological specialization diploma holders , 51 - change of institution/course
53 - Short cycle diploma holders , 57 - change of institution/course(international)


3. Application_order - dtype = Integer,
Description - Application order(between 0-first choice and 9-last choice)

            
4. Course -  dtype = Integer,
Description - 33 - Biofuel Production Technologies ,171 - Animation and Multimedia Design, 8014 - Social Service (evening attendance) 9003 - Agronomy 9070 - Communication Design 9085 - Veterinary Nursing 9119 - Informatics Engineering 9130 - Equinculture 9147 - Management 9238 - Social Service 9254 - Tourism 9500 - Nursing 9556 - Oral Hygiene 9670 - Advertising and Marketing Management 9773 - Journalism and Communication 9853 - Basic Education 9991 - Management (evening attendance)          

            
5. Daytime_evening - dtype = Integer
Description - 1 - daytime , 0 - evening

            
6. Previous_qualification - 1 - Secondary education ,2 - Higher education - bachelor's degree, 3 - Higher education - degree, 4 - Higher education - master's, 
         5 - Higher education - doctorate, 6 - Frequency of higher education 9 - 12th year of schooling - not completed, 10 - 11th year of schooling - not completed ,12 - Other - 11th year of schooling, 
        14 - 10th year of schooling ,15 - 10th year of schooling - not completed ,19 - Basic education 3rd cycle (9th/10th/11th year) or equiv, 38 - Basic education 2nd cycle (6th/7th/8th year) or equiv ,
        39 - Technological specialization course ,40 - Higher education - degree (1st cycle), 42 - Professional higher technical course, 43 - Higher education - master (2nd cycle

            
7. Nationality - dtype - Integer, 
   Description - 1 - Portuguese; 2 - German; 6 - Spanish; 11 - Italian; 13 - Dutch; 14 - English; 17 - Lithuanian; 21 - Angolan; 22 - Cape Verdean; 24 - Guinean; 25 - Mozambican; 26 - Santomean; 32 - Turkish; 41 - Brazilian; 62 - Romanian; 100 - Moldova (Republic of); 101 - Mexican; 103 - Ukrainian; 105 - Russian; 108 - Cuban; 109 - Colombian


8. Mother_qualification - dtype - Integer ,
   Description - 1 - Secondary Education - 12th Year of Schooling or Eq.,
             2 - Higher Education - Bachelor's Degree, 3 - Higher Education - Degree ,
            4 - Higher Education - Master's,
             5 - Higher Education - Doctorate ,
            6 - Frequency of Higher Education, 9 - 12th Year of Schooling - Not Completed, 10 - 11th Year of Schooling - Not Completed,
             11 - 7th Year (Old) ,12 - Other - 11th Year of Schooling ,14 - 10th Year of Schooling ,18 - General commerce course ,
            19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.,
             22 - Technical-professional course ,
            26 - 7th year of schooling 27 - 2nd cycle of the general high school course ,29 - 9th Year of Schooling - Not Completed ,
            30 - 8th year of schooling ,34 - Unknown ,35 - Can't read or write ,36 - Can read without having a 4th year of schooling ,37 - Basic education 1st cycle (4th/5th year) or equiv.,
             38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv., 39 - Technological specialization course, 40 - Higher education - degree (1st cycle), 41 - Specialized higher studies course,
             42 - Professional higher technical course ,43 - Higher Education - Master (2nd cycle), 44 - Higher Education - Doctorate (3rd cycle)
            
9. Father_qualification - dtype - Integer ,
   Description -1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 13 - 2nd year complementary high school course 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 20 - Complementary High School Course 22 - Technical-professional course 25 - Complementary High School Course - not concluded 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 31 - General Course of Administration and Commerce 33 - Supplementary Accounting and Administration 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle)


10. Mother_occupation - dtype - Integer , 
    Description - 0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 122 - Health professionals 123 - teachers 125 - Specialists in information and communication technologies (ICT) 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 171 - Skilled construction workers and the like, except electricians 173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like 175 - Workers in food processing, woodworking, clothing and other industries and crafts 191 - cleaning workers 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants
            

11. Father_occupation - dtype - Integer ,
    Description - 0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 101 - Armed Forces Officers 102 - Armed Forces Sergeants 103 - Other Armed Forces personnel 112 - Directors of administrative and commercial services 114 - Hotel, catering, trade and other services directors 121 - Specialists in the physical sciences, mathematics, engineering and related techniques 122 - Health professionals 123 - teachers 124 - Specialists in finance, accounting, administrative organization, public and commercial relations 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 135 - Information and communication technology technicians 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 154 - Protection and security services personnel 161 - Market-oriented farmers and skilled agricultural and animal production workers 163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence 171 - Skilled construction workers and the like, except electricians 172 - Skilled workers in metallurgy, metalworking and similar 174 - Skilled workers in electricity and electronics 175 - Workers in food processing, woodworking, clothing and other industries and crafts 181 - Fixed plant and machine operators 182 - assembly workers 183 - Vehicle drivers and mobile equipment operators 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants 195 - Street vendors (except food) and street service providers

            
12. Displaced - dtype - Integer ,
    Description - 1 - yes , 0 - no
            
13. Educational_special_needs - dtype - Integer,
    Description - 1 - yes 0 - no
            
14. Debtor - dtype - Integer ,
    Description - 1 - yes 0 - no
            
15. Tuition_fees_up_to_date - dtype - Integer ,
    Description - 1 - yes 0 - no
            

16. Scholarship_holder - dtype - Integer ,
    Description - 1 - yes 0 - no
            
17. Age_at_enrollment  - dtype - Integer , 
    Description - Age of studend at enrollment


18. International - dtype - Integer ,
    Description -  1 - yes 0 - no  


19. Curricular_units_1st_sem_credited - d-type - Integer ,
    Description -  Number of curricular units credited in the 1st semester


20. Curricular_units_1st_sem_enrolled - d-type - Integer ,
    Description -  	Number of curricular units enrolled in the 1st semester


21. Curricular_units_1st_sem_evaluations - dtype - Integer ,
    Description - Number of evaluations to curricular units in the 1st semester

            
22. Curricular_units_1st_sem_approved - dtype - Integer ,
    Description - Number of curricular units approved in the 1st semester


23. Curricular_units_1st_sem_grade - dtype - float ,
    Description - Grade average in the 1st semester (between 0 and 20)


24. Curricular_units_1st_sem_without evaluations - dtype - Integer ,
    Description - Number of curricular units without evalutions in the 1st semester

25. Curricular_units_2nd_sem_credited - dtype - Integer ,
    Description -  Number of curricular units credited in the 2nd semester
            
26. Curricular_units_2nd_sem_enrolled - dtype - Integer ,
    Description - Number of curricular units enrolled in the 2nd semester
            

27. Curricular_units_2nd_sem_evaluations - dtype - Integer ,
    Description - Number of evaluations to curricular units in the 2nd semester
            
28. Curricular_units_2nd_sem_approved - dtype - Integer ,
    Description - 	Number of curricular units approved in the 2nd semester
            

29. Curricular_units_2nd_sem_grade - dtype - float ,
    Description - Grade average in the 2nd semester (between 0 and 20)
            

30. Curricular_units_2nd_sem_without evaluations - dtype - Integer ,
    Description - Number of curricular units without evalutions in the 1st semester
            

31. Unemployment_rate - dtype - float ,
    Description - Unemployment rate (%)
            
32. Inflation_rate - dtype - float ,
    Description - Inflation rate (%)
            
33. GDP - dtype - float ,
    Description - GDP
            
            
    """)