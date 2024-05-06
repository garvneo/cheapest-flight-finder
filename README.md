# cheapest-flight-finder

# Flight Deal Notifier - A Python Project for Finding Cheap Flights

This repo holds Flight Deal Notifier project, a Python application designed to locate budget-friendly flight options and send personal text messages to interested users.

## Tools Used:

- **Python:** Primary programming language for application development.
- **Libraries:**
  - `requests`: Facilitates API requests to external services.
  - `datetime`: Enables manipulation of date and time objects.
  - `pprint`: Utilized for pretty-printing data structures, mainly for debugging purposes.
- **External APIs:**
  - Tequila API: Employed for flight searches based on specified criteria. [Tequila API](https://tequila.kiwi.com/)
  - Twilio : For sending messages to mobile phone.
- **Other:**
  - `dotenv`: Manages environment variables securely, including API keys.

## Learning from this Project:

- **API Integrations:** Demonstrates interaction with external APIs using the `requests` library.
- **Data Management:** Utilizes a `DataManager` class for reading and writing data from a local file, with potential for extension to utilize Google Sheets API.
- **Error Handling:** Implements basic error handling in the `FlightSearch.check_flights` method to handle potential `IndexError` exceptions during JSON parsing.
- **Conditional Logic:** Utilizes conditional statements to assess flight prices and initiate notifications based on user-defined thresholds.
- **Twilio Integration:** Implement SMS notifications through Twilio API for users preferring this communication method.
- **Google Sheets API Integration:** Store and manage flight data in a Google Sheet for collaborative editing and streamlined data access.
- **Advanced Error Handling:** Enhance error handling to capture various exceptions and provide comprehensive user feedback.
- **Deployment:** Deploy the application to a cloud platform like Heroku for automated execution and scheduling.

## Running the Project:

1. Clone this repository.
2. Install required libraries: `pip install requests` (and any additional libraries as needed).
3. Set up environment variables for API keys using dotenv.
4. Ensure `data_manager.py` points to the correct location of your data file (or configure Google Sheets API).
5. Run `main.py` to initiate the flight search and notification process.

