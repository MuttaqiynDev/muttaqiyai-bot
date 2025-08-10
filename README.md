# Telegram AI Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-green.svg)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue.svg)

**Powerful Telegram bot powered by Google Gemini AI**

[Get Started](#-installation) • [Features](#-features) • [ Configuration](#️-configuration) • [Usage](#-usage)

</div>

---

## About The Project

This Telegram bot leverages **Google Gemini AI** technology to provide intelligent responses to user queries. The bot manages users through an SQLite database and includes an admin panel for broadcasting messages to all users.

## Features

### AI-Powered Responses
- **Gemini 2.5 Pro** model integration
- Intelligent answers to any questions
- HTML-formatted response display
- Real-time "typing..." indicator

### User Management
- Automatic user registration
- SQLite database storage
- User statistics tracking
- Persistent user data

### Admin Panel
- Broadcast messages to all users
- User statistics dashboard
- Admin privilege verification
- Mass communication tools

## Installation

### Prerequisites
- Python 3.13
- Telegram Bot Token
- Google Gemini API Key

### Clone the Repository
```bash
git clone https://github.com/MuttaqiynDev/muttaqiyai-bot.git
cd muttaqiyai-bot
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Settings
Edit the following variables in the code:
```python
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"  
ADMIN_ID = "YOUR_TELEGRAM_ID_HERE"
```

## Usage

### Start the Bot
```bash
python main.py
```

### Available Commands

| Command | Description | Access Level |
|---------|-------------|--------------|
| `/start` | Initialize the bot | All users |
| `/id` | Get your Telegram ID | All users |
| `/users` | View user statistics | Admin only |
| `/sendall` | Broadcast message | Admin only |

## Bot Functionality

### Regular Users

**Getting Started**
- Use `/start` command to initialize the bot
- Receive a personalized welcome message
- Get automatically registered in the database

**AI Chat**
- Send any text message to the bot
- AI processes your query using Gemini
- Receive intelligent, contextual responses
- See "⏳ Writing..." status during processing

**ID Retrieval**
- Use `/id` command to get your Telegram ID
- Useful for admin configuration

### Admin Features

**Statistics**
- `/users` - View total registered users count
- Monitor bot usage and growth

**Broadcasting**
- `/sendall Your message here` - Send messages to all users
- Receive delivery report with success count
- Error handling for inactive users

## Getting API Keys

### Telegram Bot Token
1. Visit [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` command
3. Follow prompts to create your bot
4. Copy the provided token

### Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

### Getting Your Telegram ID
1. Message [@userinfobot](https://t.me/userinfobot)
2. Start the bot
3. Copy your user ID from the response

## 📁 Project Structure

```
muttaqiyai-bot/
│
├── main.py              # Main bot application
├── users.db           # SQLite database (auto-generated)
├── README.md          # Project documentation
└── requirements.txt   # Dependencies list
```

## Technical Details

### Dependencies
- **aiogram** - Modern Telegram Bot API framework
- **google-generativeai** - Google Gemini AI integration
- **sqlite3** - Built-in database management
- **asyncio** - Asynchronous programming support

### Database Schema
```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY
);
```

### Architecture
- **Asynchronous**: Built with async/await for optimal performance
- **Modular**: Clean separation of concerns
- **Scalable**: SQLite database for user management
- **Error Handling**: Comprehensive exception management

## Troubleshooting

### Common Issues

**❌ "Invalid token" Error**
```
Cause: Incorrect bot token
Solution: Verify TELEGRAM_BOT_TOKEN is correct
```

**❌ "API key invalid" Error**
```
Cause: Invalid Gemini API key
Solution: Check and update GEMINI_API_KEY
```

**❌ "Permission denied" Error**
```
Cause: Incorrect admin ID
Solution: Verify ADMIN_ID matches your Telegram ID
```

**❌ Database Issues**
```
Cause: SQLite permission problems
Solution: Ensure write permissions in bot directory
```

## 🔄 Version History

### v1.0.0 (Current)
- ✅ Core AI functionality with Gemini 2.5 Pro
- ✅ User registration and management
- ✅ Admin control panel
- ✅ Broadcasting system
- ✅ Error handling and logging

### Planned Features
- 🔄 Advanced user analytics
- 🔄 Message history
- 🔄 Custom AI prompts

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow Python PEP 8 style guide
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation as needed

---

## Show Your Support

If you found this project helpful, please consider:
- Starring the repository
- Forking for your own use
- Reporting bugs or issues
- Suggesting new features

## Contact & Support

- **Developer**: [@MuttaqiynDev](https://t.me/MuttaqiynDev)
- **Channel**: [@Muttaqiyn_Media](https://t.me/MuttaqiynDev_uz)
- **Issues**: [GitHub Issues](https://github.com/MuttaqiyndDev/muttaqiyai-bot/issues)

## Useful Links

- [Aiogram Documentation](https://docs.aiogram.dev/)
- [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Python SQLite Tutorial](https://docs.python.org/3/library/sqlite3.html)

---

<div align="center">

**⭐ Don't forget to star this repo if you found it useful!**

Made with by [@MuttaqiynDev](https://t.me/MuttaqiynDev)

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=MuttaqiynDev.muttaqiyai-bot)

</div>
