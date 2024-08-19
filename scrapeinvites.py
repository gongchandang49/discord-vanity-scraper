import requests
import json


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://discord.com',
    'Referer': 'https://discord.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Chromium";v="126","Google Chrome";v="126","Not A(Brand";v="99"', 
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-algolia-api-key': 'aca0d7082e4e63af5ba5917d5e96bed0',
    'x-algolia-application-id': 'NKTZZ4AIZU',
}

# Add one or more keywords as you prefer
wordlist = ["games", "sports"]

# This list was provided by ChatGPT. If you can make it generate more (beware of duplicates) or find a smarter way to generate keywords, feel free to share it.
# ["Sports", "Football", "Basketball", "Soccer", "Baseball", "Hockey", "Tennis", "Golf", "Cricket", "Rugby", "Wrestling", "Boxing", "MMA", "Motorsports", "Formula 1", "NASCAR", "Cycling", "Swimming", "Athletics", "Gymnastics", "Esports", "Gaming", "Video Games", "PC Gaming", "Console Gaming", "Mobile Gaming", "MMORPG", "FPS", "MOBA", "RPG", "Strategy Games", "Simulation Games", "Adventure Games", "Indie Games", "Retro Games", "Speedrunning", "Twitch", "YouTube", "Streaming", "Content Creation", "Art", "Drawing", "Painting", "Digital Art", "Photography", "Design", "Graphic Design", "3D Modeling", "Animation", "Music", "Musicians", "Bands", "Composers", "Rock", "Pop", "Hip-Hop", "Rap", "Jazz", "Classical Music", "Electronic Music", "EDM", "DJing", "Instruments", "Guitar", "Piano", "Drums", "Violin", "Singing", "Songwriting", "Music Production", "Dance", "Choreography", "Hip-Hop Dance", "Ballet", "Breakdance", "Theatre", "Acting", "Filmmaking", "Movies", "TV Shows", "Anime", "Manga", "Comics", "Marvel", "DC Comics", "Superheroes", "Cosplay", "Cartoons", "Disney", "Pixar", "Star Wars", "Harry Potter", "Lord of the Rings", "Game of Thrones", "The Witcher", "Sherlock Holmes", "Doctor Who", "Stranger Things", "Friends", "The Office", "Brooklyn Nine-Nine", "Sitcoms", "Drama", "Thriller", "Horror", "Science Fiction", "Fantasy", "Romance", "Crime", "Documentaries", "History", "Mythology", "Literature", "Books", "Novels", "Fiction", "Non-Fiction", "Poetry", "Short Stories", "Writing", "Fanfiction", "Journaling", "Blogs", "Creative Writing", "Storytelling", "Language Learning", "English", "Spanish", "French", "German", "Italian", "Japanese", "Korean", "Chinese", "Russian", "Programming", "Coding", "Web Development", "Software Development", "Game Development", "Data Science", "Machine Learning", "Artificial Intelligence", "Cybersecurity", "Hacking", "Tech News", "Gadgets", "Smartphones", "Computers", "Laptops", "Tablets", "Wearables", "Virtual Reality", "Augmented Reality", "Blockchain", "Cryptocurrency", "Bitcoin", "Ethereum", "NFTs", "Investing", "Finance", "Stock Market", "Economics", "Business", "Entrepreneurship", "Startups", "Marketing", "Social Media", "Influencers", "Blogging", "Vlogging", "Travel", "Adventure", "Backpacking", "Hiking", "Camping", "Road Trips", "Culture", "Food", "Cooking", "Baking", "Recipes", "Restaurants", "Healthy Eating", "Vegan", "Vegetarian", "Fitness", "Workouts", "Bodybuilding", "Yoga", "Meditation", "Wellness", "Mental Health", "Self-Care", "Lifestyle", "Fashion", "Beauty", "Makeup", "Skincare", "Haircare", "Nails", "Jewelry", "Accessories", "Watches", "Shoes", "Streetwear", "Luxury", "Vintage", "Thrifting", "Sustainability", "Eco-Friendly", "Minimalism", "Interior Design", "Home Decor", "DIY", "Crafting", "Woodworking", "Gardening", "Plants", "Nature", "Wildlife", "Animals", "Pets", "Dogs", "Cats", "Birds", "Aquariums", "Fishkeeping", "Reptiles", "Insects", "Exotic Pets", "Horse Riding", "Equestrian", "Cars", "Automobiles", "Motorcycles", "Boats", "Planes", "Trains", "Public Transport", "Urban Exploration", "Architecture", "Engineering", "Robotics", "Space", "Astronomy", "Astrophysics", "Science", "Biology", "Physics", "Chemistry", "Mathematics", "Statistics", "Geography", "Geology", "Meteorology", "Climate Change", "Environment", "Ecology", "Conservation", "Marine Biology", "Zoology", "Genetics", "Biotechnology", "Philosophy", "Ethics", "Religion", "Spirituality", "Christianity", "Islam", "Hinduism", "Buddhism", "Judaism", "Paganism", "Witchcraft", "Astrology", "Tarot", "Numerology", "Mindfulness", "Health", "Nutrition", "Self-Improvement", "Motivation", "Productivity", "Goal Setting", "Time Management", "Organization", "Life Hacks", "Education", "Learning", "Teaching", "School", "College", "University", "Scholarships", "Study Tips", "Exams", "Career", "Job Hunting", "Resumes", "Interviews", "Freelancing", "Remote Work", "Work-Life Balance", "Leadership", "Management", "Networking", "Public Speaking", "Communication", "Social Skills", "Relationships", "Dating", "Marriage", "Family", "Parenting", "Childcare", "Friendship", "Community", "Socializing", "Volunteering", "Activism", "Social Justice", "Charity", "Politics", "Government", "Elections", "Law", "Legal Advice", "Investigations", "True Crime", "World History", "Ancient History", "Medieval History", "Modern History", "War", "Military", "Weapons", "Tactics", "Strategy", "Diplomacy", "International Relations", "Current Events", "News", "Media", "Journalism", "Editing", "Publishing", "Authors", "Poets", "Playwrights", "Philosophers", "Scientists", "Inventors", "Explorers", "Artists", "Painters", "Sculptors", "Photographers", "Filmmakers", "Actors", "Directors", "Producers", "Singers", "Writers", "Survival", "Prepping", "Outdoors", "Climbing", "Fishing", "Hunting", "Birdwatching", "Videography", "Film", "Television", "Podcasts", "Tabletop Games", "Board Games", "Card Games", "Role-Playing Games", "Dungeons and Dragons", "Magic: The Gathering", "Pokemon", "Yu-Gi-Oh!", "Memes", "Humor", "Jokes", "Stand-Up Comedy", "Sketch Comedy", "Improvisation", "Magic", "Illusions", "Puzzles", "Brain Teasers", "Trivia", "Quizzes", "Riddles", "Logic Puzzles", "Sudoku", "Crosswords", "Word Games", "App Development", "Tech", "3D Printing", "Big Data", "Sculpting", "Crafts", "Home Improvement", "Technology"]

for word in wordlist:
    data = {"query": word,"filters":"auto_removed:false AND approximate_presence_count> 0 AND approximate_member_count>200","optionalFilters":["preferred_locale: en-US"],"length":1000,"offset":0,"restrictSearchableAttributes":["name","description","keywords","categories.name","categories.name_localizations.en-US","primary_category.name","primary_category.name_localizations.en-US","vanity_url_code"]}

    response = requests.post(
        'https://nktzz4aizu-dsn.algolia.net/1/indexes/prod_discoverable_guilds/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.23.3)%3B%20Browser',
        headers=headers,
        data=json.dumps(data),
    )

    json_data = response.json()
    hits = json_data['hits']
    for item in hits:
        invite = item['vanity_url_code']
        # If you print the full "item", you can see other data from the servers like ID, name, etc.
        #serverid = item['id']
        if invite is not None:
            print(f"{invite}")