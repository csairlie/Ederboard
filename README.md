# Ederboard 🏆
### Host automated endorsement leaderboards on Ed Discussions

![](https://github.com/csairlie/Ederboard/blob/main/tutorial.gif)

## 🚀 Features
- Leaderboard updates automatically on any specified schedule
- Multi-course support
- Supports endorsed threads, comments, and answers
- Deploy in the cloud with Docker

## 🔨 Dependencies
- [edapi](https://github.com/smartspot2/edapi/tree/master)

## 💾 Installation
- Install edapi from [pip](https://pypi.org/project/edapi/)
- [Retrieve your Ed Discussion API Key](https://edstem.org/us/settings/api-tokens)
- Run main.py to start.
  
## 🐋 Run with Docker
- Clone the repository
- Build the image: ```docker build -t ederboard .```
- Run the container: ```docker run -i ederboard```

## 👀 Coming soon...
- Support for endorsed comment/answer usernames
- Support for realtime local & cloud databases for leaderboard querying
