def generate_response(message):

    if "data" in message or "analysis" in message: 
        return "You might enjoy a career in Data Analysis. Look into learning Python, SQL, and tools lie Power BI and Tableau."
    elif "Web" in message or "frontend" in message: 
        return "Web deelopment could a real possibility for you! Start with HTML, CSS, JAVASCRIPT, and a frontend framework like React."
    elif "hardware" in message or "electronics" in message: 
        return "You might be interested in Embedded Systems or Computer Engineering. Consider learning Arduine, C/C++, and microcontrollers. "
    elif "ai" in message or "machine learning" in message:
        return "AI and Machine Learning are exciting fields. Learn Python, NumPy, Pandas, Scikit-learn, and Tensorflow."
    elif "backend" in message or "server" in message: 
        return "Backend Development could be your thing . Learn Python(Flask, Django), Node.js, databases like PostgreSQL or MangoDB. "
    else:
        return "Tell me more about your interests or skills so I can guide you better. For example, say things like I like building websites or I like analyzing data."