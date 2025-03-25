Main Idea: Professional Networking App to automate and speed up my job search networking workflow.

Context: I am currently searching for my first job. I have a background in economics and data science, went to prestigious schools and got good grades. I am a high achiever and have set my sights on getting a high paying job in tech, ai, consulting or some other exciting, high-paying field. I am looking for data science, product management or ai consulting/solution architect type roles. I am doing a lot of networking, primarily through LinkedIn, with friends, friends of friends, family, and school alumni. 

Current Workflow: My current networking flow is to find an alumni or potential connection who works at a company I'm interested in, or has a job I'm interested in, and connect with them on linkedin. I then send them a message with a quick introduction and asking if they'd be open to a short call. If they say yes, I schedule the call/coffee chat, then create a doc i call my "Conversation Prep Guide" that has my goals for the call, thoughtful, insightful questions to ask, a tailored "about me" section I can reference when i introduce myself, and some background research on the company, their hiring practices (timeline, open roles, desired qualifications, etc.). I then take notes during the call on this doc and then have an llm summarize my notes in a short paragraph and prepare a thank you note/follow up. I store this paragraph, as well as the connection's name, contact info., date of the call, and whether I have sent a thank you in a google sheet.

Goal: My networking workflow is pretty time consuming and repetitive. I want to build an ai agent to help automate it. Importantly however, I want the messages it writes to be in my writing style. Slightly informal, very appreciative, thoughtful, excited/energetic, inquisitive and kind. I can provide the agent information about me like my linkedin, resume, a few cover letters and other "about me" content i have written in the past as well as prior outreach messages i have sent. 

Desired Workflow: 
Step 1: Manually upload a PDF of the person I want to network with's LinkedIn profile to the app. 
Step 2: Agent analyzes the profile and uses its knowledge base of my prior outreach messages, resume, and writing samples to draft an outreach message. I then can converse back and forth with the agent to edit the message.
Step 3: Once I am satisfied with the message, I will approve it. The app should then update my networking tracker Google Sheet with the person's name and the outreach message I approved.
Step 4: I will manually message the person on LinkedIn.
Step 5: I will manually respond to and replies and schedule the conversation if applicable.
Step 6: Once I have the meeting scheduled, I will go into the app and it should help me prepare for the conversation. To do so, it should first prompt me to upload the person's profile again as well as ask me what my goals are for the conversation. Once I have provided these, it should create a "Conversation Prep Guide" that matches the format of the examples I have provided and included in its knowledge base.
Step 7: It should create this "Conversation Prep Guide" as a google doc and save it in my Google Drive Folder "Informational Interview Notes". It should update my Google Sheets tracker with a link to the Prep Guide for that person.
Step 8: For during the actual interview, I should be able to turn on a feature in the app that transcribes the conversation and then generates notes from the transcription.
Step 9: It should then automatically generate a summary of the conversation from the transcription/notes as well as a Thank You/Follow Up Message that I can send to the person.
Step 10: It should update my Google Sheets tracker with the conversation summary
Step 11: I will manually send the follow up and update the Google Sheets tracker that the Thank You has been sent. If it has been 12 hours since the call and I have not updated the tracker, the app should email me a reminder to send the thank you.

Implementation specifications/ideas:
- let's just keep the front end simple and use streamlit
- for the backend, let's use python
- For the AI agent, let's use Open AI's responses AI and agents SDK. I have a custom gpt i have set up if we can make api calls to that, but if not we can just start from scratch (https://platform.openai.com/docs/api-reference/responses)
- For the conversation transcription let's use Open AI's new Audio API (https://platform.openai.com/docs/api-reference/audio)

Frontend Design Idea:
- For now, just a single page
- 5 main sections
    1. Chat section: Biggest section, right in the middle, should look like a typical chatbot interface. Input box with an enter button to send the chat, scrollable with previous messages and responses able to be seen above, button to start a new chat, button to start recording (for transcription)

    2. Workflow Tracker Status section: Skinnier section, To the right of the chat section. Should be like a roadmap of the networking workflow with all of the steps laid out in order and an indication as to which step this particular chat is at (outreach, conversation prep, thank you, etc.)

    3. Knowledge Base Section: Top left. Should have a button to add a new document to the knowledge base (should only add it to the knowledge base of the current chat). Should also have a clickable dropdown menu that lists the documents that are currently in the knowledge base. There should be some default documents that are always loaded in the knowledge base for every new chat (like my resume, "About Me", writing samples, etc.), but other documents that are chat-specific that i will need to upload (i.e. the connection's linkedin profile, maybe notes from previous conversations, etc.)

    4. Important links Section. Middle left. Should have links to my LinkedIn profile, my Google Sheets tracker, and my google drive folder where I store my conversation prep guides

    5. Chat History section. bottom left. Should be like how chatGPT has previous chats in a sidebar. I should be able to click on them and open them. They should also have a status indicator that shows where that specific chat is at in the overall workflow (step 2, step 5, etc.)