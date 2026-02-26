import google.generativeai as genai
import os

# 1. Configuración de la API
os.environ["GEMINI_API_KEY"] = "TU_API_KEY"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def analyze_flight_safety(metar_report, flight_hours):
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Act as an Aviation Safety Expert. Analyze the following METAR weather report 
    for a student pilot with {flight_hours} flight hours.
    
    METAR Report: {metar_report}
    
    Provide a report in English including:
    1. Decoded Weather: (Wind, Visibility, Clouds in plain English).
    2. Risk Assessment: (Is it safe for a student pilot?).
    3. Final Recommendation: (Go or No-Go decision).
    """
    
    response = model.generate_content(prompt)
    return response.text

# 2. Ejemplo de METAR 
current_weather = "SADF 262000Z 12015G25KT 9999 FEW030 25/15 Q1013"

# 3. Ejecución usando tus datos reales
print("--- AI Aviation Safety Analysis ---")
safety_report = analyze_flight_safety(current_weather, 15)
print(safety_report)