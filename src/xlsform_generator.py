import pandas as pd
import openpyxl
from openpyxl import load_workbook
import os
import json

def extract_template_metadata(template_path):
    """
    Extracts the column structures (headers) from the template to provide 
    the AI agent with a precise schema for form creation.
    """
    if not os.path.exists(template_path):
        return None
    
    wb = load_workbook(template_path, data_only=True)
    metadata = {}
    
    target_sheets = ['survey', 'choices', 'settings', 'entities']
    for sheet in target_sheets:
        if sheet in wb.sheetnames:
            ws = wb[sheet]
            # Get the first row (headers)
            headers = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1, values_only=True))[0]]
            metadata[sheet] = headers
            
    return metadata

def generate_xlsform(output_path, survey_data, choices_data, settings_data, template_path=None):
    """
    Generates an ODK XLSForm .xlsx file.
    
    Instead of deleting sheets, this version creates a clean file based on 
    the extracted schema or a fresh workbook, ensuring no template data 
    leaks into the final form.
    """
    
    # 1. Handle the Workbook
    # We create a new workbook to ensure zero contamination from template data.
    # If a template is provided, we only use it to copy the 'reference' sheets.
    wb = openpyxl.Workbook()
    
    # Remove the default sheet created by openpyxl
    default_sheet = wb.active
    wb.remove(default_sheet)

    # 2. Copy Reference Sheets from Template (if available)
    if template_path and os.path.exists(template_path):
        template_wb = load_workbook(template_path, data_only=True)
        # Only copy sheets that are NOT the data sheets
        data_sheets = {'survey', 'choices', 'settings', 'entities'}
        for sheet_name in template_wb.sheetnames:
            if sheet_name not in data_sheets:
                # Create a new sheet in our target wb and copy values
                ws_new = wb.create_sheet(sheet_name)
                ws_old = template_wb[sheet_name]
                for row in ws_old.iter_rows(values_only=True):
                    ws_new.append(row)

    # 3. Write Survey Data
    ws_survey = wb.create_sheet('survey', 0)
    for row in survey_data:
        ws_survey.append(row)

    # 4. Write Choices Data
    ws_choices = wb.create_sheet('choices', 1)
    for row in choices_data:
        ws_choices.append(row)

    # 5. Write Settings Data
    ws_settings = wb.create_sheet('settings', 2)
    # Headers
    headers = list(settings_data.keys())
    ws_settings.append(headers)
    # Values
    ws_settings.append(list(settings_data.values()))

    wb.save(output_path)

if __name__ == "__main__":
    # Example usage
    template = "templates/odk_template.xlsx"
    
    # Extract schema for AI precision
    schema = extract_template_metadata(template)
    print("Extracted Schema for AI Agent:")
    print(json.dumps(schema, indent=2))
    
    survey_cols = schema['survey'] if schema else ['type', 'name', 'label']
    survey_rows = [['text', 'name', 'What is your name?']]
    
    choices_cols = schema['choices'] if schema else ['list_name', 'name', 'label']
    choices_rows = [['gender', '1', 'Male'], ['gender', '2', 'Female']]
    
    settings = {'form_title': 'Test Form', 'form_id': 'test_v1', 'version': '1'}
    
    generate_xlsform(
        'test_output.xlsx', 
        [survey_cols] + survey_rows, 
        [choices_cols] + choices_rows, 
        settings,
        template_path=template
    )
    print("\nClean XLSForm generated successfully.")
