import os
import shutil
import findfiles


base_path ='I:\Research Coordinators\Data Cleaning\JHH\Coordinator Cleaning Files'
final_path = findfiles.list_contents(base_path)
current_files = os.listdir(final_path)
names = ['JHH_AdultED_Blood','JHH_AdultED_Oral','JHH_PedED_Blood',
         'JHH_PedED_Oral']

adult_blood = ""
adult_oral = ""
peds_blood = ""
peds_oral = ""
redform = ""
for name in current_files:
    if name.startswith('JHH_AdultED_Blood'):
        adult_blood = final_path + "\\" + name
        if os.path.isfile('Adult_blood.xls'):
            os.remove('Adult_blood.xls')
        shutil.copyfile(adult_blood,'Adult_blood.xls')
        
    if name.startswith('JHH_AdultED_Oral'):
        adult_oral = final_path + "\\" + name
        if os.path.isfile('Adult_oral.xls'):
            os.remove('Adult_oral.xls')
        shutil.copyfile(adult_oral,'Adult_oral.xls')
    if name.startswith('JHH_Ped_Blood'):
        peds_blood = final_path + "\\" + name
        if os.path.isfile('Peds_blood.xls'):
            os.remove('Peds_blood.xls')
        shutil.copyfile(peds_blood,'Peds_blood.xls')
    if name.startswith('JHH_PedED_Oral'):
        peds_oral = final_path + "\\" + name
        if os.path.isfile('Peds_oral.xls'):
            os.remove('Peds_oral.xls')
        shutil.copyfile(peds_oral,'Peds_oral.xls')
    if name.lower().startswith('redform'):
        redform = final_path + "\\" + name
        if os.path.isfile('Current_Months_Red_Form_Data.xls'):
            os.remove('Current_Months_Red_Form_Data.xls')
        shutil.copyfile(redform, 'Current_Months_Red_Form_Data.xls')
