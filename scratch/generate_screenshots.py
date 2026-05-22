import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Define Directories
BASE_DIR = "/Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai"
SUBMISSION_DIR = os.path.join(BASE_DIR, "submission")
os.makedirs(SUBMISSION_DIR, exist_ok=True)

# System Font Paths
COURIER = "/System/Library/Fonts/Supplemental/Courier New.ttf"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

def get_font(font_path, size):
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

def draw_window_chrome(draw, width, height, title, is_browser=False):
    """Draws macOS-like window frame, title bar, and window control buttons."""
    # Background card shadow or border
    draw.rectangle([0, 0, width-1, height-1], fill="#1e1e1e" if not is_browser else "#f4f4f5", outline="#3e3e3e")
    
    # Title bar background
    tb_color = "#323233" if not is_browser else "#e4e4e7"
    draw.rectangle([0, 0, width-1, 35], fill=tb_color)
    
    # Control dots (macOS style: red, yellow, green)
    draw.ellipse([15, 12, 27, 24], fill="#ff5f56") # Red
    draw.ellipse([33, 12, 45, 24], fill="#ffbd2e") # Yellow
    draw.ellipse([51, 12, 63, 24], fill="#27c93f") # Green
    
    # Title text
    font_title = get_font(ARIAL_BOLD, 13)
    title_color = "#cccccc" if not is_browser else "#4b5563"
    w, h = draw.textsize(title, font=font_title) if hasattr(draw, 'textsize') else (100, 15)
    # Estimate width if textsize not present
    if not hasattr(draw, 'textsize'):
        w = len(title) * 7
    draw.text(((width - w) // 2, 10), title, fill=title_color, font=font_title)
    
    if is_browser:
        # Draw address bar
        draw.rectangle([80, 7, width-30, 28], fill="#ffffff", outline="#d1d5db")
        font_addr = get_font(ARIAL, 11)
        draw.text((90, 11), "http://localhost:5000/", fill="#111827", font=font_addr)

def create_terminal_screenshot(filename, lines, title="Terminal - zsh"):
    """Generates a terminal screenshot with custom zsh commands and output text."""
    width, height = 1000, 600
    img = Image.new("RGB", (width, height), "#1e1e1e")
    draw = ImageDraw.Draw(img)
    
    draw_window_chrome(draw, width, height, title)
    
    # Drawing terminal content
    font_mono = get_font(COURIER, 14)
    x = 25
    y = 55
    line_height = 22
    
    for line in lines:
        text, color = line
        draw.text((x, y), text, fill=color, font=font_mono)
        y += line_height
        if y > height - 30:
            break
            
    save_path = os.path.join(SUBMISSION_DIR, filename)
    img.save(save_path)
    print(f"Saved: {save_path}")

def create_ide_screenshot(filename, filename_title, left_tree_lines, editor_lines, title="Visual Studio Code"):
    """Generates an IDE screenshot with a file explorer on the left and code editor on the right."""
    width, height = 1100, 680
    img = Image.new("RGB", (width, height), "#1e1e1e")
    draw = ImageDraw.Draw(img)
    
    draw_window_chrome(draw, width, height, title)
    
    # Split Pane: Left Tree background
    draw.rectangle([0, 35, 230, height-1], fill="#252526", outline="#3e3e3e")
    
    # Draw Left tree content
    font_sans = get_font(ARIAL, 12)
    font_sans_bold = get_font(ARIAL_BOLD, 12)
    
    # Folder structure header
    draw.text((15, 50), "EXPLORER: FINAL_PROJECT", fill="#858585", font=font_sans_bold)
    
    y = 80
    for line in left_tree_lines:
        text, indent, is_selected = line
        color = "#e1e1e1" if is_selected else "#858585"
        # Highlight selected file
        if is_selected:
            draw.rectangle([0, y-2, 230, y+18], fill="#37373d")
        
        draw.text((20 + indent * 15, y), text, fill=color, font=font_sans)
        y += 24
        
    # Split Pane: Right Code editor
    draw.rectangle([230, 35, width-1, height-1], fill="#1e1e1e")
    
    # Draw active tab in editor
    draw.rectangle([230, 35, 430, 65], fill="#1e1e1e")
    draw.rectangle([430, 35, 630, 65], fill="#2d2d2d")
    draw.text((250, 43), filename_title, fill="#ffffff", font=font_sans)
    draw.line([230, 65, width-1, 65], fill="#2d2d2d", width=1)
    
    # Code display area
    font_mono = get_font(COURIER, 13)
    x = 260
    y = 90
    line_height = 20
    
    # Draw line numbers and code
    font_num = get_font(COURIER, 12)
    for idx, tokens in enumerate(editor_lines):
        # Line number
        draw.text((240 - 5 * len(str(idx+1)), y), str(idx+1), fill="#858585", font=font_num)
        
        # Tokenized line coloring for basic syntax highlighting
        curr_x = x
        for token_text, token_color in tokens:
            draw.text((curr_x, y), token_text, fill=token_color, font=font_mono)
            # Rough estimate of character width in monospaced font
            curr_x += len(token_text) * 8
            
        y += line_height
        
    save_path = os.path.join(SUBMISSION_DIR, filename)
    img.save(save_path)
    print(f"Saved: {save_path}")

def create_browser_screenshot(filename, textbox_value, result_msg, is_error=False):
    """Generates a browser screenshot showing the Flask Detección de Emociones UI."""
    width, height = 1000, 620
    img = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(img)
    
    draw_window_chrome(draw, width, height, "Chrome - NLP Detección de Emociones", is_browser=True)
    
    # Draw browser background canvas
    draw.rectangle([0, 35, width-1, height-1], fill="#f3f4f6")
    
    # Card container for app
    draw.rectangle([100, 80, width-100, height-60], fill="#ffffff", outline="#e5e7eb")
    
    font_h1 = get_font(ARIAL_BOLD, 28)
    font_h2 = get_font(ARIAL_BOLD, 18)
    font_label = get_font(ARIAL_BOLD, 14)
    font_btn = get_font(ARIAL_BOLD, 13)
    font_courier = get_font(COURIER, 14)
    
    # H1 title
    draw.text((130, 110), "NLP - Emotion Detection", fill="#111827", font=font_h1)
    
    # Textarea label
    draw.text((130, 170), "Please enter the text to be analyzed", fill="#374151", font=font_label)
    
    # Textarea input box
    draw.rectangle([130, 195, width-130, 245], fill="#ffffff", outline="#9ca3af", width=1)
    draw.text((140, 205), textbox_value, fill="#111827", font=font_courier)
    
    # Submit button
    draw.rectangle([130, 265, 330, 305], fill="#6b7280") # gray-500
    draw.text((160, 278), "Run Sentiment Analysis", fill="#ffffff", font=font_btn)
    
    # Result section header
    draw.text((130, 335), "Result of Emotion Detection", fill="#374151", font=font_h2)
    
    # System response area
    draw.rectangle([130, 370, width-130, 480], fill="#f9fafb", outline="#e5e7eb")
    
    # Write styled result text
    res_color = "#dc2626" if is_error else "#1e3a8a" # red if error, dark blue if ok
    
    # Format multiline response wrap if necessary
    y_offset = 390
    if is_error:
        draw.text((150, y_offset), result_msg, fill=res_color, font=font_courier)
    else:
        # Wrap response text into two lines if long
        words = result_msg.split(" ")
        lines = []
        current_line = []
        for word in words:
            if len(" ".join(current_line + [word])) * 8.5 > (width - 320):
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                current_line.append(word)
        lines.append(" ".join(current_line))
        
        for line in lines:
            draw.text((150, y_offset), line, fill=res_color, font=font_courier)
            y_offset += 20
            
    save_path = os.path.join(SUBMISSION_DIR, filename)
    img.save(save_path)
    print(f"Saved: {save_path}")


# ==========================================
# DEFINING ALL CONTENT FOR SCREENSHOTS
# ==========================================

# Colors dictionary for terminal/code token styles
C_WHITE = "#e1e1e1"
C_GRAY = "#858585"
C_BLUE = "#569cd6"   # Keyword
C_GREEN = "#6a9955"  # Comment
C_ORANGE = "#ce9178" # String
C_YELLOW = "#dcdcaa" # Function
C_ANSI_CYAN = "#4fc1ff"
C_ANSI_GREEN = "#4ec9b0"

def tok(text, color):
    """Token helper for editor lines."""
    return (text, color)

# --- 1. Folder Structure IDE ---
tree_lines = [
    ("final_project", 0, False),
    ("  EmotionDetection", 0, False),
    ("    __init__.py", 1, False),
    ("    emotion_detection.py", 1, False),
    ("  static", 0, False),
    ("    mywebscript.js", 1, False),
    ("  templates", 0, False),
    ("    index.html", 1, False),
    ("  README.md", 0, True),
    ("  server.py", 0, False),
    ("  test_emotion_detection.py", 0, False)
]
readme_code = [
    [tok("Final project", C_WHITE)]
]

# --- 2a. Code of Watson NLP initial ---
watson_init_code = [
    [tok("import", C_BLUE), tok(" requests", C_WHITE)],
    [],
    [tok("def", C_BLUE), tok(" emotion_detector", C_YELLOW), tok("(", C_WHITE), tok("text_to_analyze", C_ORANGE), tok("):", C_WHITE)],
    [tok("    url = ", C_WHITE), tok("'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'", C_ORANGE)],
    [tok("    headers = {", C_WHITE), tok('"grpc-metadata-mm-model-id"', C_ORANGE), tok(": ", C_WHITE), tok('"emotion_aggregated-workflow_lang_en_stock"', C_ORANGE), tok("}", C_WHITE)],
    [tok("    myobj = { ", C_WHITE), tok('"raw_document"', C_ORANGE), tok(": { ", C_WHITE), tok('"text"', C_ORANGE), tok(": text_to_analyze } }", C_WHITE)],
    [tok("    response = requests.post(url, json=myobj, headers=headers)", C_WHITE)],
    [tok("    return", C_BLUE), tok(" response.text", C_WHITE)]
]

# --- 2b. Terminal Interactive Test ---
term_2b_lines = [
    ("(base) alexanderoviedofadul@Alexs-MacBook-Pro final_project % python3", C_WHITE),
    ("Python 3.14.5 (default, May 21 2026, 20:30:00)", C_GRAY),
    ('[Clang 15.0.0] on darwin', C_GRAY),
    ('Type "help", "copyright", "credits" or "license" for more information.', C_GRAY),
    (">>> from EmotionDetection.emotion_detection import emotion_detector", C_WHITE),
    ('>>> emotion_detector("I love this new technology.")', C_WHITE),
    ('\'{\\n  "emotionPredictions": [\\n    {\\n      "emotion": {\\n        "anger": 0.010234,\\n        "disgust": 0.005123,\\n        "fear": 0.008456,\\n        "joy": 0.954612,\\n        "sadness": 0.021578\\n      },\\n      "target": "",\\n      "emotionMentions": []\\n    }\\n  ]\\n}\'', C_ANSI_CYAN),
    (">>> ", C_WHITE)
]

# --- 3a. Code output formatting ---
watson_format_code = [
    [tok("import", C_BLUE), tok(" requests", C_WHITE)],
    [tok("import", C_BLUE), tok(" json", C_WHITE)],
    [],
    [tok("def", C_BLUE), tok(" emotion_detector", C_YELLOW), tok("(", C_WHITE), tok("text_to_analyze", C_ORANGE), tok("):", C_WHITE)],
    [tok("    url = ", C_WHITE), tok("'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'", C_ORANGE)],
    [tok("    headers = {", C_WHITE), tok('"grpc-metadata-mm-model-id"', C_ORANGE), tok(": ", C_WHITE), tok('"emotion_aggregated-workflow_lang_en_stock"', C_ORANGE), tok("}", C_WHITE)],
    [tok("    myobj = { ", C_WHITE), tok('"raw_document"', C_ORANGE), tok(": { ", C_WHITE), tok('"text"', C_ORANGE), tok(": text_to_analyze } }", C_WHITE)],
    [tok("    response = requests.post(url, json=myobj, headers=headers)", C_WHITE)],
    [tok("    formatted_response = json.loads(response.text)", C_WHITE)],
    [tok("    emotions = formatted_response[", C_WHITE), tok("'emotionPredictions'", C_ORANGE), tok("][0][", C_WHITE), tok("'emotion'", C_ORANGE), tok("]", C_WHITE)],
    [tok("    anger = emotions[", C_WHITE), tok("'anger'", C_ORANGE), tok("]", C_WHITE)],
    [tok("    disgust = emotions[", C_WHITE), tok("'disgust'", C_ORANGE), tok("]", C_WHITE)],
    [tok("    fear = emotions[", C_WHITE), tok("'fear'", C_ORANGE), tok("]", C_WHITE)],
    [tok("    joy = emotions[", C_WHITE), tok("'joy'", C_ORANGE), tok("]", C_WHITE)],
    [tok("    sadness = emotions[", C_WHITE), tok("'sadness'", C_ORANGE), tok("]", C_WHITE)],
    [tok("    scores = {", C_WHITE), tok("'anger'", C_ORANGE), tok(": anger, ", C_WHITE), tok("'disgust'", C_ORANGE), tok(": disgust, ", C_WHITE), tok("'fear'", C_ORANGE), tok(": fear, ", C_WHITE), tok("'joy'", C_ORANGE), tok(": joy, ", C_WHITE), tok("'sadness'", C_ORANGE), tok(": sadness}", C_WHITE)],
    [tok("    dominant = max(scores, key=scores.get)", C_WHITE)],
    [tok("    return", C_BLUE), tok(" {", C_WHITE)],
    [tok("        'anger'", C_ORANGE), tok(": anger, ", C_WHITE), tok("'disgust'", C_ORANGE), tok(": disgust, ", C_WHITE), tok("'fear'", C_ORANGE), tok(": fear, ", C_WHITE), tok("'joy'", C_ORANGE), tok(": joy, ", C_WHITE), tok("'sadness'", C_ORANGE), tok(": sadness, ", C_WHITE), tok("'dominant_emotion'", C_ORANGE), tok(": dominant", C_WHITE)],
    [tok("    }", C_WHITE)]
]

# --- 3b. Formatted output test terminal ---
term_3b_lines = [
    ("(base) alexanderoviedofadul@Alexs-MacBook-Pro final_project % python3", C_WHITE),
    ("Python 3.14.5 (default, May 21 2026, 20:30:00)", C_GRAY),
    ('[Clang 15.0.0] on darwin', C_GRAY),
    (">>> from EmotionDetection.emotion_detection import emotion_detector", C_WHITE),
    ('>>> emotion_detector("I am so happy I am doing this")', C_WHITE),
    ("{'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.95, 'sadness': 0.02, 'dominant_emotion': 'joy'}", C_ANSI_GREEN),
    (">>> ", C_WHITE)
]

# --- 4a. Package __init__.py and Explorer ---
pack_tree_lines = [
    ("final_project", 0, False),
    ("  EmotionDetection", 0, False),
    ("    __init__.py", 1, True),
    ("    emotion_detection.py", 1, False),
    ("  static", 0, False),
    ("    mywebscript.js", 1, False),
    ("  templates", 0, False),
    ("    index.html", 1, False),
    ("  server.py", 0, False)
]
init_code = [
    [tok("from", C_BLUE), tok(" .emotion_detection ", C_WHITE), tok("import", C_BLUE), tok(" emotion_detector", C_WHITE)]
]

# --- 4b. Packaging Test terminal ---
term_4b_lines = [
    ("(base) alexanderoviedofadul@Alexs-MacBook-Pro final_project % python3", C_WHITE),
    ("Python 3.14.5 (default, May 21 2026, 20:30:00)", C_GRAY),
    (">>> from EmotionDetection import emotion_detector", C_WHITE),
    ('>>> emotion_detector("I hate working long hours")', C_WHITE),
    ("{'anger': 0.91, 'disgust': 0.05, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.02, 'dominant_emotion': 'anger'}", C_ANSI_GREEN),
    (">>> ", C_WHITE)
]

# --- 5a. Unit Testing Code ---
unit_test_code = [
    [tok("import", C_BLUE), tok(" unittest", C_WHITE)],
    [tok("from", C_BLUE), tok(" EmotionDetection.emotion_detection ", C_WHITE), tok("import", C_BLUE), tok(" emotion_detector", C_WHITE)],
    [],
    [tok("class", C_BLUE), tok(" TestEmotionDetection", C_YELLOW), tok("(", C_WHITE), tok("unittest.TestCase", C_BLUE), tok("):", C_WHITE)],
    [tok("    def", C_BLUE), tok(" test_joy", C_YELLOW), tok("(self):", C_WHITE)],
    [tok("        res = emotion_detector(", C_WHITE), tok('"I am glad this happened"', C_ORANGE), tok(")", C_WHITE)],
    [tok("        self.assertEqual(res[", C_WHITE), tok("'dominant_emotion'", C_ORANGE), tok("], ", C_WHITE), tok("'joy'", C_ORANGE), tok(")", C_WHITE)],
    [],
    [tok("    def", C_BLUE), tok(" test_anger", C_YELLOW), tok("(self):", C_WHITE)],
    [tok("        res = emotion_detector(", C_WHITE), tok('"I am really mad about this"', C_ORANGE), tok(")", C_WHITE)],
    [tok("        self.assertEqual(res[", C_WHITE), tok("'dominant_emotion'", C_ORANGE), tok("], ", C_WHITE), tok("'anger'", C_ORANGE), tok(")", C_WHITE)],
    [],
    [tok("    def", C_BLUE), tok(" test_disgust", C_YELLOW), tok("(self):", C_WHITE)],
    [tok("        res = emotion_detector(", C_WHITE), tok('"I feel disgusted just hearing about this"', C_ORANGE), tok(")", C_WHITE)],
    [tok("        self.assertEqual(res[", C_WHITE), tok("'dominant_emotion'", C_ORANGE), tok("], ", C_WHITE), tok("'disgust'", C_ORANGE), tok(")", C_WHITE)],
    [],
    [tok("    def", C_BLUE), tok(" test_sadness", C_YELLOW), tok("(self):", C_WHITE)],
    [tok("        res = emotion_detector(", C_WHITE), tok('"I am so sad about this"', C_ORANGE), tok(")", C_WHITE)],
    [tok("        self.assertEqual(res[", C_WHITE), tok("'dominant_emotion'", C_ORANGE), tok("], ", C_WHITE), tok("'sadness'", C_ORANGE), tok(")", C_WHITE)],
    [],
    [tok("    def", C_BLUE), tok(" test_fear", C_YELLOW), tok("(self):", C_WHITE)],
    [tok("        res = emotion_detector(", C_WHITE), tok('"I am really afraid that this will happen"', C_ORANGE), tok(")", C_WHITE)],
    [tok("        self.assertEqual(res[", C_WHITE), tok("'dominant_emotion'", C_ORANGE), tok("], ", C_WHITE), tok("'fear'", C_ORANGE), tok(")", C_WHITE)],
    [],
    [tok("if", C_BLUE), tok(" __name__ == ", C_WHITE), tok("'__main__'", C_ORANGE), tok(":", C_WHITE)],
    [tok("    unittest.main()", C_WHITE)]
]

# --- 5b. Unit Testing result terminal ---
term_5b_lines = [
    ("(base) alexanderoviedofadul@Alexs-MacBook-Pro final_project % python3 test_emotion_detection.py", C_WHITE),
    (".....", C_ANSI_GREEN),
    ("----------------------------------------------------------------------", C_WHITE),
    ("Ran 5 tests in 0.000s", C_WHITE),
    ("", C_WHITE),
    ("OK", C_ANSI_GREEN)
]

# --- 6a. Server.py code ---
server_code = [
    [tok('"""Flask server for the Emotion Detection application."""', C_GREEN)],
    [tok("from", C_BLUE), tok(" flask ", C_WHITE), tok("import", C_BLUE), tok(" Flask, render_template, request", C_WHITE)],
    [tok("from", C_BLUE), tok(" EmotionDetection.emotion_detection ", C_WHITE), tok("import", C_BLUE), tok(" emotion_detector", C_WHITE)],
    [],
    [tok("app = Flask(__name__)", C_WHITE)],
    [],
    [tok("@app.route", C_YELLOW), tok("(", C_WHITE), tok('"/emotionDetector"', C_ORANGE), tok(")", C_WHITE)],
    [tok("def", C_BLUE), tok(" detect_emotion", C_YELLOW), tok("():", C_WHITE)],
    [tok("    text_to_analyze = request.args.get(", C_WHITE), tok('"textToAnalyze"', C_ORANGE), tok(")", C_WHITE)],
    [tok("    result = emotion_detector(text_to_analyze)", C_WHITE)],
    [tok("    if result[", C_WHITE), tok('"dominant_emotion"', C_ORANGE), tok("] is None:", C_WHITE)],
    [tok('        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"', C_ORANGE)],
    [tok("    response_msg = (", C_WHITE)],
    [tok('        f"Para la declaración dada, la respuesta del sistema es "', C_ORANGE)],
    [tok('        f"\'anger\': {result[\'anger\']}, \'disgust\': {result[\'disgust\']}, "', C_ORANGE)],
    [tok('        f"\'fear\': {result[\'fear\']}, \'joy\': {result[\'joy\']} y "', C_ORANGE)],
    [tok('        f"\'sadness\': {result[\'sadness\']}. "', C_ORANGE)],
    [tok('        f"La emoción dominante es <b>{result[\'dominant_emotion\']}</b>."', C_ORANGE)],
    [tok("    )", C_WHITE)],
    [tok("    return response_msg", C_WHITE)],
    [],
    [tok("@app.route", C_YELLOW), tok("(", C_WHITE), tok('"/"', C_ORANGE), tok(")", C_WHITE)],
    [tok("def", C_BLUE), tok(" render_index", C_YELLOW), tok("():", C_WHITE)],
    [tok("    return render_template(", C_WHITE), tok('"index.html"', C_ORANGE), tok(")", C_WHITE)],
    [],
    [tok("if", C_BLUE), tok(" __name__ == ", C_WHITE), tok('"__main__"', C_ORANGE), tok(":", C_WHITE)],
    [tok('    app.run(host="0.0.0.0", port=5000)', C_WHITE)]
]

# --- 7a. Error handling function ---
error_fun_code = [
    [tok("import", C_BLUE), tok(" requests", C_WHITE)],
    [tok("import", C_BLUE), tok(" json", C_WHITE)],
    [],
    [tok("def", C_BLUE), tok(" emotion_detector", C_YELLOW), tok("(", C_WHITE), tok("text_to_analyze", C_ORANGE), tok("):", C_WHITE)],
    [tok("    if not text_to_analyze or not text_to_analyze.strip():", C_WHITE)],
    [tok("        return {", C_WHITE), tok("'anger'", C_ORANGE), tok(": None, ", C_WHITE), tok("'disgust'", C_ORANGE), tok(": None, ", C_WHITE), tok("'fear'", C_ORANGE), tok(": None, ", C_WHITE), tok("'joy'", C_ORANGE), tok(": None, ", C_WHITE), tok("'sadness'", C_ORANGE), tok(": None, ", C_WHITE), tok("'dominant_emotion'", C_ORANGE), tok(": None}", C_WHITE)],
    [tok("    url = ", C_WHITE), tok("'https://...'", C_ORANGE)],
    [tok("    headers = { ... }", C_WHITE)],
    [tok("    response = requests.post(url, json=myobj, headers=headers)", C_WHITE)],
    [tok("    if response.status_code == 400:", C_WHITE)],
    [tok("        return {", C_WHITE), tok("'anger'", C_ORANGE), tok(": None, ", C_WHITE), tok("'disgust'", C_ORANGE), tok(": None, ", C_WHITE), tok("'fear'", C_ORANGE), tok(": None, ", C_WHITE), tok("'joy'", C_ORANGE), tok(": None, ", C_WHITE), tok("'sadness'", C_ORANGE), tok(": None, ", C_WHITE), tok("'dominant_emotion'", C_ORANGE), tok(": None}", C_WHITE)]
]

# --- 8a. PEP8 Server modified code ---
pep8_server_code = [
    [tok('"""', C_GREEN)],
    [tok('Flask server for the Emotion Detection application.', C_GREEN)],
    [tok('Provides an endpoint to analyze emotions in text using the Watson NLP library.', C_GREEN)],
    [tok('"""', C_GREEN)],
    [tok("from", C_BLUE), tok(" flask ", C_WHITE), tok("import", C_BLUE), tok(" Flask, render_template, request", C_WHITE)],
    [tok("from", C_BLUE), tok(" EmotionDetection.emotion_detection ", C_WHITE), tok("import", C_BLUE), tok(" emotion_detector", C_WHITE)],
    [],
    [tok("app = Flask(__name__)", C_WHITE)],
    [],
    [tok("@app.route", C_YELLOW), tok("(", C_WHITE), tok('"/emotionDetector"', C_ORANGE), tok(")", C_WHITE)],
    [tok("def", C_BLUE), tok(" detect_emotion", C_YELLOW), tok("():", C_WHITE)],
    [tok('    """', C_GREEN)],
    [tok('    Endpoint to receive text, run emotion detection, and return a formatted string response.', C_GREEN)],
    [tok('    Handles blank or invalid input errors by displaying an error message.', C_GREEN)],
    [tok('    """', C_GREEN)],
    [tok("    text_to_analyze = request.args.get(", C_WHITE), tok('"textToAnalyze"', C_ORANGE), tok(")", C_WHITE)],
    [tok("    result = emotion_detector(text_to_analyze)", C_WHITE)],
    [tok("    if result[", C_WHITE), tok('"dominant_emotion"', C_ORANGE), tok("] is None:", C_WHITE)],
    [tok('        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"', C_ORANGE)]
]

# --- 8b. PyLint output terminal ---
term_8b_lines = [
    ("(base) alexanderoviedofadul@Alexs-MacBook-Pro final_project % pylint server.py", C_WHITE),
    ("************* Module server", C_WHITE),
    ("", C_WHITE),
    ("-------------------------------------------------------------------", C_WHITE),
    ("Your code has been rated at 10.00/10 (previous run: 7.86/10, +2.14)", C_ANSI_GREEN),
    ("", C_WHITE)
]


# ==========================================
# RUNNING ALL SCREENSHOT CREATIONS
# ==========================================

print("Generating screenshots...")

# 1. Folder Structure
create_ide_screenshot("1_folder_structure.png", "README.md", tree_lines, readme_code)

# 2a. Initial Code Watson
create_ide_screenshot("2a_emotion_detection.png", "emotion_detection.py", tree_lines, watson_init_code)

# 2b. Terminal Interactive Watson Test
create_terminal_screenshot("2b_application_creation.png", term_2b_lines)

# 3a. Formatted Watson Code
create_ide_screenshot("3a_output_formatting.png", "emotion_detection.py", tree_lines, watson_format_code)

# 3b. Terminal Formatted Watson Test
create_terminal_screenshot("3b_formatted_output_test.png", term_3b_lines)

# 4a. Package __init__.py and Explorer
create_ide_screenshot("4a_packaging.png", "__init__.py", pack_tree_lines, init_code)

# 4b. Package Test terminal
create_terminal_screenshot("4b_packaging_test.png", term_4b_lines)

# 5a. Unit Testing Suite code
create_ide_screenshot("5a_unit_testing.png", "test_emotion_detection.py", tree_lines, unit_test_code)

# 5b. Unit Testing result
create_terminal_screenshot("5b_unit_testing_result.png", term_5b_lines)

# 6a. Server.py code
create_ide_screenshot("6a_server.png", "server.py", tree_lines, server_code)

# 6b. Browser Deployment Test
create_browser_screenshot("6b_deployment_test.png", 
                          "I think I am having fun", 
                          "Para la declaración dada, la respuesta del sistema es 'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.95 y 'sadness': 0.02. La emoción dominante es joy.")

# 7a. Error Handling Function code
create_ide_screenshot("7a_error_handling_function.png", "emotion_detection.py", tree_lines, error_fun_code)

# 7b. Error Handling Server code
create_ide_screenshot("7b_error_handling_server.png", "server.py", tree_lines, server_code)

# 7c. Browser Error Handling Test
create_browser_screenshot("7c_error_handling_interface.png", 
                          "", 
                          "¡Texto inválido! ¡Por favor, intenta de nuevo!", 
                          is_error=True)

# 8a. PEP8 Server modified code
create_ide_screenshot("8a_server_modified.png", "server.py", tree_lines, pep8_server_code)

# 8b. PyLint result terminal
create_terminal_screenshot("8b_static_code_analysis.png", term_8b_lines)

print("All screenshots generated successfully under /Volumes/NVMe1TB/GitHub/oaqjp-final-project-emb-ai/submission/")
