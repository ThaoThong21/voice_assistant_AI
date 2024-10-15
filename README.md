# Voice Assistant AI

This project integrates a voice assistant AI with Asterisk to monitor incoming calls and interact with users through an automated system.

## Installation Instructions

### Step 1: Install Asterisk
To install Asterisk, follow the official installation guide:

- [Prerequisites for PJSIP and PJProject](https://docs.asterisk.org/Getting-Started/Installing-Asterisk/Installing-Asterisk-From-Source/Prerequisites/PJSIP-pjproject/)
- [Download Asterisk source code](https://www.asterisk.org/downloads/source-code/)

I used **Asterisk 21** for this project. After installing, you will need to configure Asterisk as described below.

### Step 2: Configuration Files

The configuration files are located in the `config` directory of this repository. These include necessary settings for PJSIP and ARI integration.

### Asterisk Model Configuration

The following users are configured in Asterisk:

- **User1**: 6001
- **User2**: 6002
- **User3**: 6003
- **Agent**: 7000

### Monitoring Calls

The system is set up to monitor all incoming calls to **User1 (6001)**. My voice assistant AI will detect the incoming calls and respond accordingly — it is designed to clone conversations using AI technology.

### Step 3: Enabling ARI (Asterisk REST Interface)

ARI is enabled to allow HTTP-based control and execution of scripts within the Call Center. This feature will enable our AI to interact with calls in real-time.

### Step 4: Softphone Setup

For users to call each other, we use **MicroSIP**, an open-source softphone.

- Download MicroSIP from the official site: [https://www.microsip.org/](https://www.microsip.org/)
- After downloading, run the `.exe` file to set up the softphone for use.

This softphone will be used by the users (e.g., User1, User2, User3) to place calls, and our system will monitor and assist these calls through the voice assistant AI.

---

## Summary

1. Install and configure Asterisk.
2. Monitor all calls to 6001, where the AI voice assistant will interact.
3. Enable ARI for HTTP control.
4. Use MicroSIP for calling between users.
