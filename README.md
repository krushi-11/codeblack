# Jarvis- A SMart Mirror
## Smart Mirror with Voice Assistant

A modern Smart Mirror implementation featuring a voice-controlled assistant that runs in the background, providing an interactive and hands-free experience.

## Features

- Real-time weather display
- Calendar integration
- News headlines
- Clock and date display
- Voice control capabilities
- Customizable widgets
- Background voice assistant for hands-free operation
- Motion sensor support for power management

## Prerequisites

### Hardware Requirements
- Raspberry Pi 4 (recommended) or 3B+
- Two-way mirror or acrylic mirror
- LCD display (recommended: 24" or larger)
- USB microphone
- Speakers
- PIR motion sensor (optional)
- Monitor frame or custom-built frame
- Power supply
- HDMI cable

### Software Requirements
- Raspberry Pi OS (64-bit recommended)
- Python 3.8+
- Node.js 14+
- Speech recognition library
- Text-to-speech engine
- Web server (nginx recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smart-mirror.git
cd smart-mirror
```

2. Install system dependencies:
```bash
sudo apt-get update
sudo apt-get install -y python3-pip nodejs npm portaudio19-dev
sudo apt-get install -y python3-pyaudio
```

3. Install Node.js dependencies:
```bash
npm install
```

## Voice Assistant Setup

1. Install voice recognition dependencies:
```bash
pip3 install speech_recognition
pip3 install pyttsx3
pip3 install openai-whisper
```

2. Configure audio devices:
```bash
# List audio devices
arecord -l
# Update audio configuration in config.yml with your device ID
```

## Running the Application

1. Start the main application:
```bash
python3 Jarvis.py
```

## Voice Commands

The voice assistant responds to the following commands:
- "Show weather"
- "Show calendar"
- "Read news headlines"
- "Turn display on/off"
- "Update calendar"
- "Set reminder [time] [message]"
- "Play music"

Add custom commands by editing `Jarvis.py`.

## Autostart on Boot

1. Create a startup script:
```bash
sudo nano /etc/systemd/system/smart-mirror.service
```

2. Add the following content:
```ini
[Unit]
Description=Smart Mirror Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/smart-mirror/start.py
WorkingDirectory=/path/to/smart-mirror
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

3. Enable the service:
```bash
sudo systemctl enable smart-mirror
sudo systemctl start smart-mirror
```

## Troubleshooting

### Common Issues

1. Voice Assistant Not Responding
   - Check microphone connections
   - Verify audio device configuration
   - Test microphone with `arecord -d 5 test.wav`

2. Display Issues
   - Verify HDMI connection
   - Check display rotation settings
   - Confirm resolution settings

3. Module Errors
   - Verify API keys in config.yml
   - Check internet connectivity
   - Review module logs in `/var/log/smart-mirror/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Magic Mirror project for inspiration
- Voice recognition community
- All contributors and testers

## Support

For support and questions:
- Create an issue in the repository
- Join our Discord community
- Check the wiki for detailed documentation

## Updates and Maintenance

Keep your Smart Mirror up to date:
```bash
git pull origin main
pip3 install -r requirements.txt
npm install
sudo systemctl restart smart-mirror
```
