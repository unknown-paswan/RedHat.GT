import pyttsx3
import datetime
import webbrowser
import wikipedia #pip install wikipedia
import speech_recognition as sr #pip install speechRecognition
# Initialize pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function to pronounce the string
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the current time
def greet_user(name):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning " + name )
    elif 12 <= hour < 18:
        speak("Good afternoon " + name )
    else:
        speak("Good evening " + name )

def handle_query(query):
    # Perform NLP processing to identify the problem and provide relevant solutions
    if 'accommodation' in query:
        response = "There are various accommodation options in Andaman and Nicobar Islands ranging from luxury resorts to budget hotels. Some popular places to stay include Port Blair, Havelock Island, and Neil Island."
    elif 'transportation' in query or 'getting around' in query or 'transport' in query:
        response = "To get around the islands, you can hire taxis, auto-rickshaws, or motorcycles. There are also ferry services available for inter-island travel. It's recommended to book transportation in advance, especially during peak tourist seasons."
    elif 'attractions' in query or 'sightseeing' in query:
        response = "Andaman and Nicobar Islands offer a range of attractions such as Cellular Jail, Radhanagar Beach, Ross Island, Baratang Island, and various water sports activities like scuba diving and snorkeling. Make sure to plan your itinerary accordingly."
    elif 'weather' in query or 'climate' in query:
        response = "The islands have a tropical climate. The best time to visit is between November and May when the weather is pleasant and suitable for outdoor activities. However, it's always a good idea to check the current weather conditions before planning your trip."
    elif'hii' in query or 'hello'in query or'hey' in query or 'hi'in query:
        response="Hello sir how can i help you"
    elif 'issue' in query or'trouble' in query:
        response=" Im here to help! Could you please provide more details about the problem you're facing ? "
    elif'hotel' in query or 'stay'in query:
        response="There are several options for accommodation in Andaman and Nicobar Islands. Some popular ones include Taj Exotica Resort, Fortune Resort Bay Island, Sea Shell Resort, and Symphony Palms Beach Resort. It depends on your preferences and budget"
    elif'tour' in query or 'package' in query:
        response="There are various tour operators available in Andaman and Nicobar Islands that offer sightseeing packages. Some popular ones are Andaman Holidays, Discover Andaman, and Andaman Bliss. They can provide you with guidance and customized tour packages."
    elif 'open official site' in query  or'open website' in query:
        response=webbrowser.open('https://www.viator.com/tours/Andaman-and-Nicobar-Islands/Andaman-and-Nicobar-Tour-Packages/d23571-164086P1?m=33953&supag=1239149766791469&supsc=dat-2329246664037350&supai=77446944684787&supdv=c&supnt=nt:o&suplp=157277&supli=133547&supti=dat-2329246664037350&tsem=true&supci=dat-2329246664037350&supkw=andaman%20and%20nicobar%20official%20website&msclkid=5505aef8e38b1facd6fbca8d2a4c6f3f')
    elif'famous spot' in query or 'place' in query or 'vist' in query:
        response =' 1-Port Blair ,2-Havelock Island ,3-Ross Island, 4-Baratang Island ,5-Diglipur ,6-Barren Island ,7-ittle Andaman ,8-Cinque Island -these are the top 10 best island to visit'
    elif'port blair'in query:
        response='Port Blair : The capital city and the entry point to the Andaman and Nicobar Islands. It is home to historical sites like Cellular Jail, Anthropological Museum, Samudrika Naval Marine Museum, and Corbyn '
    elif'havelock island'in query:
        response='Havelock Island : Known for its pristine beaches, especially Radhanagar Beach, which has been ranked as one of the best beaches in Asia. It offers opportunities for snorkeling, scuba diving, and water sports.'
    elif'ross island'in query:
        response='Roos Island :  Once the administrative headquarters of the British, now in ruins. It showcases the remnants of British colonial architecture and has a historical significance.'
    elif'creater'in query or 'master' in query:
        response='I am created by my master Gautam paswan'
    elif'baratang island' in query:
        response='Baratang Island: Famous for its limestone caves and mangrove forests. The journey to reach the caves involves a boat ride through the dense mangrove creeks.'
    elif'diglipur' in query:
        response='Diglipur : Located in North Andaman, it offers attractions like Ross and Smith Islands, Saddle Peak (the highest point in the islands), and Kalipur Beach.' 
    elif 'barren island'in query:
        response='Barren Island : An active volcanic island in the Andaman Sea, known for its unique ecosystem and scuba diving opportunities to witness underwater volcanic activity.'
    elif'little andaman' in query:
        response='Little Andaman : A less explored island with stunning beaches like Butler Bay Beach and Whisper Wave Waterfall. It also offers opportunities for surfing.'
    elif'long island' in query:
        response='Long Island : Known for its serene and secluded beaches like Lalaji Bay and Merk Bay. It is a perfect place for nature lovers and birdwatchers.'
    elif'cinque island:' in query:
        response='Cinque Island: A group of two islands, North Cinque and South Cinque, known for their coral reefs, clear waters, and rich marine life'
    elif'budgets' in query or'budget' in query or'Budget 'in query:
        response='Are you searching for : Hotals|Restaurant if no Enter : no'
    elif'hotals' in query or 'Hotals' in query or 'hotal'in query or 'Hotal'in query:
        response=' looking for low-budget hotels in the Andaman and Nicobar Islands, its important to consider factors such as location, amenities, and customer reviews. Here are a few suggestions for budget-friendly accommodations:'
        'Port Blair:Hotel Haywizz: Located in the heart of Port Blair, this hotel offers affordable rooms and basic amenities.Hotel Islander Inn: Situated near the airport, this budget hotel provides comfortable rooms and a convenient location.Hotel Marine View: A budget hotel located near the Cellular Jail, offering clean and comfortable rooms at affordable rates.'
        'Havelock Island:SeaShell Resort: This resort offers budget-friendly options, including cottages and rooms with basic amenities.Wild Orchid Resort: Located near the famous Radhanagar Beach, this budget resort offers comfortable accommodations.green Valley Resort: Situated in a peaceful area, this budget-friendly resort provides cozy rooms and a friendly atmosphere.'
        'Neil Island:Tango Beach Resort: Offering affordable accommodations close to the beach, this resort provides comfortable rooms with basic amenities.Sea Shell Neil: A budget-friendly resort with comfortable rooms and a great location near Bharatpur Beach.Hotel Kingfisher: Situated near the jetty, this budget hotel provides clean and comfortable rooms.'
    elif 'restaurants' in query or 'restaurant' in query:
        response='When looking for low-budget restaurants in the Andaman and Nicobar Islands, you all find various options that offer affordable and delicious meals. Here are a few suggestions: 1-Port Blair:Annapurna Restaurant: Located in Aberdeen Bazaar, this restaurant offers a variety of Indian vegetarian and non-vegetarian dishes at budget-friendly prices.Icy Spicy: Situated near the Cellular Jail, this restaurant serves North Indian, South Indian, and Chinese cuisine at reasonable rates.Light House Residency Restaurant: This restaurant, near the Cellular Jail, offers a menu with a mix of Indian and Chinese dishes at affordable prices.2-Havelock Island:Full Moon Café: Located near Beach No. 5 (Radhanagar Beach), this café serves a range of cuisines, including Indian and Continental, at reasonable prices.Something Different: Situated near Beach No. 2 (Govind Nagar Beach), this restaurant offers budget-friendly meals with a focus on seafood and Indian cuisine.3-Anju Coco Resto: Located near Beach No. 3 (Vijay Nagar Beach), this restaurant serves Indian, Chinese, and Continental dishes at affordable rates.3-Neil Island:Auntys  Restaurant: Situated near Sitapur Beach, this restaurant offers budget-friendly meals with a variety of Indian and seafood options.Garden View Restaurant: Located near Bharatpur Beach, this restaurant serves Indian, Chinese, and Continental dishes at affordable prices.Sea Shell Restaurant: Situated near Lakshmanpur Beach, this restaurant offers a range of dishes, including Indian and Continental cuisine, at reasonable rates'
    elif'food' in query or 'hungry'in query:
        response='I understand that feeling hungry can be quite challenging . are you (vegetarian),(non vegetarian),(both)'
    elif'guide' in query or 'gudiance' in query:
        response='I am suggesting you a 7 travel guide for andaman and nicobar (transport charges are excluded) - Day 1: Port Blair -Arrive at Port Blair and check into your hotel. Visit Cellular Jail and attend the "Light and Sound Show" in the evening.  Explore the local markets and indulge in some shopping. Day 2: Havelock Island Take a ferry to Havelock Island.Visit Radhanagar Beach, known for its pristine beauty and turquoise waters.  Engage in water activities like snorkeling or scuba diving.Enjoy a leisurely evening on the beach.  Day 4: Baratang Island Embark on a day trip to Baratang Island.Visit the limestone caves and marvel at their natural beauty.Witness the fascinating mud volcanoes.Explore Parrot Island during sunset. Day 5: North Bay and Ross Island Take a boat ride to North Bay Island.Engage in water activities like snorkeling or sea walking.Visit Ross Island, the former administrative headquarters of the British.Explore the ruins and enjoy the scenic views.  Day 6: Jolly Buoy Island and Red Skin Island Take a boat ride to Jolly Buoy Island (or Red Skin Island, depending on availability).Enjoy snorkeling and witness the vibrant coral reefs and marine life.Relax on the pristine beaches and soak in the beauty of the surroundings. Day 7: Port Blair and Departure Visit Anthropological Museum and Samudrika Marine Museum to learn about the islands history and biodiversity.Explore Marina Park and enjoy the sea views. Depart from Port Blair with beautiful memories of Andaman and Nicobar Islands. Please take note that you must avoid last minute booking and make sure to book the fairies in advance Here are some travel agencies you can consult: Andaman Holidays Experience Andamans Andaman Tour Travelandaman Emerald Holidays Discover Andaman Holidays'
    elif'nice'in query or 'good'in query or 'great'in query or 'wow' in query:
        response=("thank you sir :-)")
    elif'vegetarian'in query:
        response=' these are the top 10 restaurants for vegetarian. : 1- Annapurna Restaurant (Port Blair). 2-Icy Spicy (Port Blair). 3-New Lighthouse Restaurant (Port Blair). 4-Amaya - The Beachfront Restaurant (Havelock Island). 5-Barefoot at Havelock (Havelock Island). 6-Full Moon Café (Havelock Island). 7-Anju Coco Resto (Havelock Island). 8-Sea Dragon Restaurant (Neil Island). 9-Mando Restaurant (Neil Island).10-Fat Martin Café (Neil Island)'
    elif'non vegetarian'in query:
        response='These are the top 10 restaurants non-vegitarian : 1-New Lighthouse Restaurant (Port Blair).2-Anju Coco Resto (Havelock Island). 3-Bonova Cafe and Pub (Port Blair). 4-Full Moon Café (Havelock Island). 5-Red Snapper (Havelock Island). 6-Sea Dragon Restaurant (Neil Island). 7-Gagan Restaurant (Port Blair). 8-Bonova Lounge & Restaurant (Port Blair). 9-Annapurna Seafood Restaurant (Port Blair). 10-Sinclairs Bayview Restaurant (Port Blair)'
    elif'reach'in query:
        response="To reach the Andaman and Nicobar Islands, you can take a combination of air and sea transportation. Here's a general guide on how to reach the islands : By Air :-The fastest and most convenient way to reach the Andaman and Nicobar Islands is by air. The main entry point is Veer Savarkar International Airport, located in Port Blair, the capital city of the Andaman and Nicobar Islands. Several domestic airlines operate regular flights from major cities in India, such as Delhi, Chennai, Kolkata, and Bangalore, to Port Blair. The flight duration varies depending on the departure city, but it usually takes around 2-3 hours.The fastest and most convenient way to reach the Andaman and Nicobar Islands is by air. The main entry point is Veer Savarkar International Airport, located in Port Blair, the capital city of the Andaman and Nicobar Islands. Several domestic airlines operate regular flights from major cities in India, such as Delhi, Chennai, Kolkata, and Bangalore, to Port Blair. The flight duration varies depending on the departure city, but it usually takes around 2-3 hours. :By sea :-Another option is to travel to the Andaman and Nicobar Islands by sea. Ships operated by the Directorate of Shipping Services, Government of India, connect Port Blair with Kolkata, Chennai, and Vishakhapatnam. The journey by sea takes longer, ranging from 50 to 70 hours, depending on the route and weather conditions. Ships have different classes of accommodation, including air-conditioned cabins, dormitories, and seating arrangements. : It's important to note that availability and schedules of flights and ships can vary, so it's advisable to check with the respective airlines or the Directorate of Shipping Services for up-to-date information, ticket availability, and booking procedures.Additionally, upon arrival in the Andaman and Nicobar Islands, tourists need to obtain an entry permit, which can be obtained upon arrival at the airport or seaport. Indian nationals do not require a permit to visit the Andaman Islands, but a permit is required for visiting Nicobar Islands and certain tribal areas.Please ensure that you check the latest travel requirements and entry procedures as they may be subject to change."
    elif'time'in query:
        response="The best time to visit the Andaman and Nicobar Islands is during the winter season, which spans from November to February. During this time, the weather is pleasant with temperatures ranging between 20 to 30 degrees Celsius (68 to 86 degrees Fahrenheit). The skies are clear, and the humidity levels are relatively low. It is an ideal time for various outdoor activities, such as water sports, sightseeing, and exploring the pristine beaches and marine life.It's important to note that the Andaman and Nicobar Islands have a tropical climate, and they can be visited throughout the year. However, the monsoon season, which occurs from May to September, brings heavy rainfall and strong winds, which may limit some activities and water sports. The summer season, from March to May, is characterized by higher temperatures and increased humidity.Considering the overall weather conditions and tourist activities, the winter season is generally regarded as the best time to visit the Andaman and Nicobar Islands."
    elif'entry'in query or'permits' in query or'restrictions'in query:
        response='Yes, there are entry permits and certain restrictions for visiting the Andaman and Nicobar Islands. These measures are in place to maintain the ecological balance and preserve the tribal communities residing in the islands. Here are some key points regarding entry permits and restrictions: 1-Restricted Area Permit (RAP): All foreign nationals require a Restricted Area Permit (RAP) to visit the Andaman and Nicobar Islands. Indian nationals do not require a permit for visiting Port Blair, but they need a permit to visit other restricted areas in the islands. 2-'
    elif'ok'in query:
        response=":-)"
    elif'beaches' in query or 'beach' in query:
        response="The Andaman and Nicobar Islands are known for their stunning beaches with crystal-clear waters and picturesque surroundings. Here are some of the best beaches to visit in the Andaman and Nicobar Islands: 1-Radhanagar Beach (Havelock Island): Radhanagar Beach is often hailed as one of the best beaches in Asia. It boasts pristine white sands, turquoise waters, and lush greenery. The beach offers a serene and relaxing atmosphere, making it a perfect spot for sunbathing, swimming, and enjoying breathtaking sunsets. 2-Elephant Beach (Havelock Island): Elephant Beach is known for its vibrant coral reefs and diverse marine life. It's a popular spot for snorkeling and scuba diving, allowing visitors to explore the underwater world. The beach is accessible by a short boat ride from Havelock Island. 3-Kalapathar Beach (Havelock Island): Kalapathar Beach is famous for its scenic beauty, with its shoreline adorned with black rocks and trees. It offers a tranquil ambiance and is an ideal place for nature walks, photography, and enjoying the peaceful surroundings. 4-Wandoor Beach (Port Blair): Wandoor Beach is located near Port Blair and is known for its picturesque landscape and coral reefs. It serves as the gateway to the Mahatma Gandhi Marine National Park, where you can witness a rich variety of marine life through glass-bottom boat rides and snorkeling.5-Corbyn's Cove Beach (Port Blair): Located just a few kilometers from Port Blair, Corbyn's Cove Beach is a popular hangout spot for tourists. It features a long stretch of coconut palms and a sandy shoreline. Visitors can indulge in water sports activities like jet skiing, banana boat rides, and parasailing. 6-Laxmanpur Beach (Neil Island): Laxmanpur Beach is renowned for its scenic beauty and stunning sunsets. It offers panoramic views of the turquoise waters and coral reefs. During low tide, you can walk along the shore and explore the coral formations and marine life.These are just a few examples of the best beaches in the Andaman and Nicobar Islands. Each beach has its own unique charm and attractions, offering visitors a chance to relax, engage in water sports, or explore the vibrant marine ecosystem."
    elif'adventure' in query or 'water' in query:
        response="Yes, the Andaman and Nicobar Islands offer a wide range of water sports and adventure activities for visitors to enjoy. Here are some popular water sports and adventure activities you can experience in the islands: 1-Scuba Diving. 2-Snorkeling. 3-Sea WalkingSea Walking. 4-Jet Skiing. 5-Parasailing. 6-Kayaking.These are just a few examples of the water sports and adventure activities available in the Andaman and Nicobar Islands. There are many more options to choose from, such as banana boat rides, speed boating, fishing, and more. It's recommended to check with local tour operators or water sports centers for the availability and safety guidelines of these activities."
    elif'wildlife'in query or 'sanctuaries' in query or'national parks'in query or 'zoo' in query:
        response="Yes, the Andaman and Nicobar Islands are home to several wildlife sanctuaries and national parks where you can explore the rich biodiversity and unique flora and fauna. Here are some notable wildlife sanctuaries and national parks in the islands: 1-Mahatma Gandhi Marine National Park: Located near Wandoor Beach in Port Blair, Mahatma Gandhi Marine National Park is a popular destination for eco-tourism and marine life conservation. The park encompasses a group of islands with rich coral reefs, vibrant marine life, and mangrove ecosystems. Glass-bottom boat rides and snorkeling are popular activities to explore the underwater beauty of the park. 2-Mount Harriet National Park: Situated in the Ferrargunj tehsil of South Andaman Island, Mount Harriet National Park is known for its dense forests and diverse wildlife. The park offers picturesque views, trekking trails, and an opportunity to spot various species of birds, butterflies, reptiles, and mammals. 3-Saddle Peak National Park: Located in North Andaman Island, Saddle Peak National Park is known for its highest peak in the Andaman and Nicobar Islands. The park is home to a variety of flora and fauna, including the Andaman wild pig, Andaman hill myna, and several endemic plant species. Trekking through the park provides a chance to witness the natural beauty and spot wildlife. 4-Campbell Bay National Park: Situated in the Great Nicobar Island, Campbell Bay National Park is one of the largest national parks in India. It is known for its pristine rainforests, diverse bird species, and endemic wildlife. The park is accessible through special permits, and guided tours provide an opportunity to explore the unique ecosystem of the region. 5-Interview Island Wildlife Sanctuary: Located in the North Andaman Island, Interview Island Wildlife Sanctuary is a haven for nature enthusiasts. It is home to various bird species, reptiles, and mammals, including the rare dugong. The sanctuary offers trekking trails and camping opportunities for a closer experience with nature.These are just a few examples of the wildlife sanctuaries and national parks in the Andaman and Nicobar Islands. Each park showcases the natural beauty and biodiversity of the islands, providing visitors with a chance to explore and appreciate the unique ecosystems. It's important to note that some areas may have restricted access or require special permits, so it's advisable to check the regulations and seek guidance from local authorities or tour operators before visiting these protected areas."
    elif'both' in query :
        response=""
    elif'emergency' in query or'help' in query:
        response="In case of emergencies in Andaman and Nicobar Islands, you can dial the following emergency numbers: 1-Police Control Room: 100. 2-Fire Service Control Room: 101. 3-Ambulance Service: 102. 4-Emergency Disaster Management: 1077. 5-Tourist Police: +91-3192-232-414. 6-Indian Embassy in Port Blair: Phone- +91-3192-233-200 .Please remember to dial the appropriate emergency number based on the nature of the emergency. It's always a good idea to keep these numbers handy during your trip. "    
    elif'shop'in query or 'shopping' in query or 'mall' in query :
        response="Andaman and Nicobar Islands offer various shopping centers where you can explore and purchase a variety of items. Here are some popular shopping centers in the region: 1-Aberdeen Bazaar, Port Blair: This bustling market in Port Blair is known for its shops selling handicrafts, clothing, electronics, and local souvenirs. 2-Sagarika Emporium, Port Blair: Located in Port Blair, Sagarika Emporium is a government-run outlet that offers a wide range of handicrafts, shell crafts, and local artifacts. 3-MG Road, Port Blair: MG Road is a popular shopping street in Port Blair where you can find a mix of shops, restaurants, and local vendors selling clothing, jewelry, and other items. 4-Samudrika Marine Museum, Port Blair: The museum has a small gift shop where you can find marine-themed souvenirs, shells, and handicrafts. 5-Phoenix Bay Jetty, Port Blair: This area near the jetty has several small shops and stalls where you can find clothing, accessories, and local snacks. These are just a few examples, and there are more shopping options available in different areas of Andaman and Nicobar Islands. Exploring the local markets and interacting with local vendors can be a delightful experience during your visit."
    elif'theatre' in query or'cinema'in query:
        response="Andaman and Nicobar Islands do not have a cinema or movie theater as of my knowledge cutoff in September 2021. However, it's always a good idea to check for any recent developments or new establishments by referring to local directories or contacting the local tourism authorities. They can provide you with the most up-to-date information regarding cinema or movie viewing options on the islands."
    elif'bank' in query or 'banking'in query or 'atms' in query or 'atm' in query or 'ATM' in query or 'ATMS' in query or 'Bank' in query or 'Banking' in query:
        response="Yes, there are ATMs and banking facilities available on the Andaman and Nicobar Islands. In major towns like Port Blair, Havelock Island, and Neil Island, you can find ATMs where you can withdraw cash using your debit or credit cards. It's advisable to carry sufficient cash as a backup, especially when visiting remote areas or smaller islands where ATMs may be limited. Additionally, there are banking facilities such as banks and branches of nationalized banks where you can exchange currency or conduct other banking transactions."
    elif 'quit' in query or '3' in query or 'q' in query:
        response = "Thank you for using the GTM CHAT BOT. Have a great day!"
        speak(response)  # Speak the farewell message
        exit()  # Exit the
    else:
        response="I'm sorry, I couldn't understand your query. could you please rephrase it ?"
    # Speak the response
    print(response)
    speak(response)
#main function
def takeCommand2():
    query = input("Enter your query: ")
    return query
#2nd command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      audio = r.listen(source)

    try :
      print("recognizing....")
      query = r.recognize_google(audio,language='en-in')
      print(f"user said:{query}\n")
    except Exception as e:
      # print(e)
      print("say that again please.... or please check your internet connection and then restart")
      query = None
    return query

def check_internet_connection():
    import socket
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
         

#main
# Main function
def main():
    name = input("Enter your name: ")
    greet_user(name)
    speak("Please enter the mode.")
    choice = input("Select mode [OFFLINE(1)/ONlINE(2)/exit(3)]: ")

    if choice == '1':
        speak("Hello, how can I assist you?")
        while True:
            user_input = input("Enter your query or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                break
            handle_query(user_input)
    elif choice == '2':
        
        speak("You selected online mode. Please select the option givin below:")
        print("Please select the option: [for TALK-(1) for CHAT-(2)]")
        while True:
            
            g = input()
            if g == "1":
                if not check_internet_connection():
                    speak("Please check your internet connection and try again.")
                    break
                else:
                    while True:
                        query = takeCommand()
                        if query:
                            speak('Searching ...')
                            query_cleaned = query.replace("wikipedia", "")
                            results = wikipedia.summary(query_cleaned, sentences=3)
                            print(results)
                            speak(results)

                            # Ask if the user wants to continue
                            speak("Do you want to continue your query? Please say 'yes' or 'no'")
                            user_response = takeCommand2()
                            if user_response and ('yes' in user_response.lower() or '5' in user_response):
                                continue
                            elif user_response and ('no' in user_response.lower() or '3' in user_response or 'quit' in user_response.lower()):
                                speak("Exiting the program. Goodbye!")
                                break
                            else:
                                speak("Invalid response. Exiting the program. Goodbye!")
                                break
               
            elif g == "2":
                if not check_internet_connection():
                    speak("Please check your internet connection and try again.")
                    break
                else:
                    while True:
                        query = takeCommand2()
                        if query:
                            speak('Searching ...')
                            query_cleaned = query.replace("wikipedia", "")
                            results = wikipedia.summary(query_cleaned, sentences=3)
                            print(results)
                            speak(results)

                            # Ask if the user wants to continue
                            speak("Do you want to continue? Please say 'yes' or 'no'")
                            user_response = takeCommand2()
                            if user_response and ('yes' in user_response.lower() or '5' in user_response):
                                continue
                            elif user_response and ('no' in user_response.lower() or '3' in user_response or 'quit' in user_response.lower()):
                                speak("Exiting the program. Goodbye!")
                                break
                            else:
                                speak("Invalid response. Exiting the program. Goodbye!")
                                break
            else:
                speak("Invalid option. Please select again.")
    elif choice == '3':
        speak("Exiting the program. Goodbye!")
    else:
        speak("Invalid choice. Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()