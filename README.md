# AI Tool Directory Project

This project is an **AI Tool Search Engine** designed to help users quickly find AI tools across various domains such as **content creation, cybersecurity, healthcare, data analytics, and more**. 
The project allows users to search for AI tools based on their requirements and provides detailed information about each tool.

## Features

- **Search Functionality**: Users can search for AI tools by keywords (e.g., "content creation", "cybersecurity").
- **Categorized Results**: Tools are categorized into *Free*, *Trial*, and *Paid* versions to make it easier for users to find tools based on availability.
- **Tool Details**: Each tool has a detailed page that includes the name, description, category, features, URL, and limitations of the tool.
- **Responsive Design**: The site is fully responsive, adjusting to different screen sizes.

## Project Structure
AI_Ttools

├── static/

│   ├── styles.css          # CSS styles for the pages
│   ├── tool.css            # CSS for tool detail pages

├── templates/

│   ├── index.html          # Search page template
│   ├── result.html         # Search result page template
│   ├── tool_detail.html    # Tool detail page template

├── app.py                  # Main server script (Flask or any other framework used)
├── tools.json              # JSON file containing AI tools data
└── README.md               # Project documentation (this file)

How It Works:

1 - Homepage: The user can search for AI tools using the search bar.
2 - Results Page: Once the search is submitted, the results are displayed under categorized sections (Free, Trial, and Paid tools).
3 - Tool Details: The user can click on any tool from the result list to see detailed information about that tool.

How to Use:

1 - Search for AI Tools: Simply type a keyword into the search bar. The search will show relevant results categorized into free, trial, and paid tools.
2 - View Tool Details: Click on any tool in the search result to see its features, limitations, and a link to the tool's website.
3 - Back to Search: Use the Back to Search button to return to the homepage and perform another search.

Installation:
git clone https://github.com/v3nom440/AI_tool_search_engine.git
cd AI_tool_search_engine

Install dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Open the app in your browser:
http://127.0.0.1:5000

Tools.json
The tools.json file is structured as follows:

[
    {
        "name": "Tool Name",
        "category": "Free",
        "description": "Brief description of the tool.",
        "url": "https://tool-website.com",
        "limitations": "Any limitations of the tool",
        "keywords": ["keyword1", "keyword2", "keyword3"],
        "features": [
            {
                "feature": "Feature Name",
                "description": "Description of the feature"
            }
        ]
      }
]

Technologies Used:
HTML/CSS: For structuring and styling the web pages.
Python/Flask: for backend functionality.
JSON: To store and retrieve AI tool data.

Future Improvements:
User Ratings and Reviews: Add the ability for users to rate and review each AI tool.
More Categories: Expand the number of AI tool categories.
User Accounts: Add user accounts for bookmarking or saving favorite tools.

Contributing
Feel free to submit pull requests or open issues for any bugs or feature requests. Contributions are welcome!

Thank you for checking out the AI Tool search engine Project! If you have any questions or suggestions, please feel free to reach out.
