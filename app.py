from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_tools():
    # Load the tools from tools.json
    with open('data/tools.json', 'r') as f:
        data = json.load(f)
    return data['tools']

@app.route('/')
def index():
    tools = load_tools()
    return render_template('index.html', tools=tools)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Default to empty string if None
    tools = load_tools()
    free_tools = []
    trial_tools = []
    paid_tools = []

    # Categorize tools based on the type
    for tool in tools:
        if isinstance(tool, dict) and 'keywords' in tool:
            # Check if the query matches any keyword
            if query.lower() in ' '.join(tool['keywords']).lower():
                if tool.get('category') == 'Free':
                    free_tools.append(tool)
                elif tool.get('category') == 'Trial':
                    trial_tools.append(tool)
                elif tool.get('category') == 'Paid':
                    paid_tools.append(tool)

    return render_template('results.html', free_tools=free_tools, trial_tools=trial_tools, paid_tools=paid_tools)

@app.route('/tool/<tool_name>')
def tool_detail(tool_name):
    tools = load_tools()
    tool = next((t for t in tools if t['name'].lower() == tool_name.lower()), None)
    if tool is None:
        return "Tool not found", 404  # Return a 404 if the tool is not found
    return render_template('tool_description.html', tool=tool)

if __name__ == '__main__':
    app.run(debug=True)