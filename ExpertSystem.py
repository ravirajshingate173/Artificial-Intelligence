airline_schedule_dict = {
 "Flight delayed": "Check for updates on the airline's website or contact customer service for assistance.",
 "Flight canceled": "Contact the airline to reschedule your flight or arrange for alternative travel options.",
 "Gate change": "Check the airport monitors for the new gate information and proceed to the updated gate.",
 "Baggage lost": "Report the lost baggage to the airline's baggage service desk and provide necessary details for tracking.",
 "Flight overbooked": "Speak to airline staff to explore options such as compensation or alternative flights.",
 "In-flight entertainment not working": "Inform the flight attendants about the issue to see if it can be resolved or compensated.",
 "Meal preference not honored": "Speak to the flight attendants to inquire about alternative meal options if available.",
 "Seat assignment changed": "Check with the airline staff for assistance in resolving the seat assignment issue.",
 "Connection missed due to delay": "Contact the airline to arrange for alternate flight options or accommodations if necessary.",
 "Flight diverted": "Follow instructions from the flight crew and airport staff for next steps and assistance."
}
def handle_request(user_input):
 if user_input.lower() == "exit":
    return "Goodbye!"
 elif user_input in airline_schedule_dict:
    return airline_schedule_dict[user_input]
 else:
    return "I'm sorry, I don't know how to help with that problem."
def main():
    while True:
        user_input = input("What's the problem? Type 'exit' to quit. ") 
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = handle_request(user_input)
        print(response)

if __name__ == "__main__":
    main()