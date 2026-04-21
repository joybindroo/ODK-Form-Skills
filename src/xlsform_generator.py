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

    This version ensures that ONLY the essential ODK sheets (survey, choices, settings, entities)
    are present in the final output. Reference sheets from the template are explicitly excluded.
    """

    # 1. Create a brand new workbook to ensure zero contamination
    wb = openpyxl.Workbook()

    # Remove the default sheet created by openpyxl
    default_sheet = wb.active
    wb.remove(default_sheet)

    # 2. Write Survey Data
    ws_survey = wb.create_sheet('survey', 0)
    for row in survey_data:
        ws_survey.append(row)

    # 3. Write Choices Data
    ws_choices = wb.create_sheet('choices', 1)
    for row in choices_data:
        ws_choices.append(row)

    # 4. Write Settings Data
    ws_settings = wb.create_sheet('settings', 2)
    # Headers
    headers = list(settings_data.keys())
    ws_settings.append(headers)
    # Values
    ws_settings.append(list(settings_data.values()))

    # 5. Optional: Entities sheet (empty by default if not provided)
    # We create it to maintain the requested 4-sheet structure if needed,
    # or we can leave it out if no entity data is passed.
    # For now, we'll only create it if the user specifically wants it.

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
