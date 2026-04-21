import pandas as pd
import openpyxl
from openpyxl import load_workbook
import os

def generate_xlsform(output_path, survey_data, choices_data, settings_data, template_path=None):
    """
    Generates an ODK XLSForm .xlsx file.
    
    :param output_path: Path where the final .xlsx will be saved.
    :param survey_data: List of lists or DataFrame for the 'survey' sheet.
    :param choices_data: List of lists or DataFrame for the 'choices' sheet.
    :param settings_data: Dictionary for the 'settings' sheet.
    :param template_path: Path to an existing .xlsx template to preserve formatting.
    """
    
    # Create DataFrames
    df_survey = pd.DataFrame(survey_data)
    df_choices = pd.DataFrame(choices_data)
    
    # Settings are usually a single row with headers
    df_settings = pd.DataFrame([settings_data])

    if template_path and os.path.exists(template_path):
        # Load template to preserve other sheets (like '👋 Start here', '⚙️ Types', etc.)
        wb = load_workbook(template_path)
        
        # Update/Create Survey sheet
        if 'survey' in wb.sheetnames:
            std = wb['survey']
            wb.remove(std)
        wb.create_sheet('survey', 0)
        ws_survey = wb['survey']
        
        # Write Survey Data
        for r_idx, row in enumerate(df_survey.values.tolist(), 1):
            for c_idx, value in enumerate(row, 1):
                ws_survey.cell(row=r_idx, column=c_idx, value=value)
        
        # Update/Create Choices sheet
        if 'choices' in wb.sheetnames:
            std = wb['choices']
            wb.remove(std)
        wb.create_sheet('choices', 1)
        ws_choices = wb['choices']
        for r_idx, row in enumerate(df_choices.values.tolist(), 1):
            for c_idx, value in enumerate(row, 1):
                ws_choices.cell(row=r_idx, column=c_idx, value=value)
                
        # Update/Create Settings sheet
        if 'settings' in wb.sheetnames:
            std = wb['settings']
            wb.remove(std)
        wb.create_sheet('settings', 2)
        ws_settings = wb['settings']
        
        # Write Settings Headers
        headers = list(settings_data.keys())
        for c_idx, header in enumerate(headers, 1):
            ws_settings.cell(row=1, column=c_idx, value=header)
        # Write Settings Values
        for c_idx, value in enumerate(settings_data.values(), 1):
            ws_settings.cell(row=2, column=c_idx, value=value)
            
        wb.save(output_path)
    else:
        # Fallback: Create from scratch using Pandas ExcelWriter
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            df_survey.to_excel(writer, sheet_name='survey', index=False)
            df_choices.to_excel(writer, sheet_name='choices', index=False)
            df_settings.to_excel(writer, sheet_name='settings', index=False)

if __name__ == "__main__":
    # Example usage for AI Agents
    survey_cols = ['type', 'name', 'label', 'hint', 'required', 'relevant', 'appearance', 'default', 'constraint', 'constraint_message', 'calculation', 'trigger', 'choice_filter', 'parameters', 'repeat_count', 'note', 'image', 'audio', 'video']
    survey_rows = [
        ['text', 'respondent_name', 'What is your name?', '', 'yes', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['select_one gender', 'gender', 'Gender', '', 'yes', '', 'horizontal', '', '', '', '', '', '', '', '', '', '', '', ''],
    ]
    
    choices_cols = ['list_name', 'name', 'label']
    choices_rows = [
        ['gender', '1', 'Male'],
        ['gender', '2', 'Female'],
        ['gender', '3', 'Other'],
    ]
    
    settings = {
        'form_title': 'Test Form',
        'form_id': 'test_form_v1',
        'version': '20260421',
        'instance_name': 'test_v1'
    }
    
    generate_xlsform(
        'test_output.xlsx', 
        [survey_cols] + survey_rows, 
        [choices_cols] + choices_rows, 
        settings
    )
    print("XLSForm generated successfully.")
