#you can install pyVoIP package with pip
from pyVoIP.VoIP import VoIPPhone, InvalidStateError, VoIPCall, CallState
import wave

# Callback function for handling the call and capturing audio
class CallHandler:
    def __init__(self, call):
        self.call = call
        self.audio_file = wave.open("call_audio.wav", "wb")
        self.audio_file.setnchannels(1)  # Mono
        self.audio_file.setsampwidth(2)  # Sample width in bytes
        self.audio_file.setframerate(8000)  # Frame rate in Hz

    def on_progress(self, request):
        print("Call in progress")

    def on_answered(self):
        print("Call answered")

    def on_media(self, media):
        print("Media received")
        while self.call.state == CallState.ANSWERED:
            logging.info("++++++++++++++++++++++++")

            audio_data = self.call.get_audio()
            if audio_data:
                self.audio_file.writeframes(audio_data)

    def on_ended(self):
        print("Call ended")
        self.audio_file.close()

# Callback function for handling the call
import logging
logging.basicConfig(level=logging.INFO, filename="sip_log.log")

def call_callback(call: VoIPCall):
    try:
        logging.info("Call answered")

        # Open a wave file to save the audio stream
        wf = wave.open('call_audio.wav', 'wb')
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # Sample width in bytes
        wf.setframerate(8000)  # Frame rate

        # Capture audio data
        while call.state == CallState.ANSWERED:
            audio_data = call.read_audio(length=160)
            if audio_data:
                wf.writeframes(audio_data)

        wf.close()
        logging.info("Call ended")
        call.hangup()
    except InvalidStateError as e:
        logging.info("Invalid state error")
        logging.info(e)

if __name__ == "__main__":
    # Replace with your Asterisk server details
    sip_server_ip = "172.24.22.183"
    sip_server_port = 5060
    sip_username = "6003"
    sip_password = "123456"
    destination_number = "7000"

    # Initialize the VoIP phone
    phone = VoIPPhone(
        sip_server_ip,
        sip_server_port,
        sip_username,
        sip_password,
        # callCallback=call_callback,
        myIP="172.24.22.183",  # Replace with your local IP
        sipPort=50604,  # Default SIP port
        rtpPortLow=10000,  # Low end of the RTP port range
        rtpPortHigh=20000  # High end of the RTP port range
    )

    # Start the phone
    logging.info("Start the phone")

    phone.start()

    # Make the call
    _call = phone.call(destination_number)
    # _call.answer()
    import time
    while _call.state == CallState.DIALING:
        time.sleep(0.1)
    print("............", _call.state)
    call_callback(_call)

    # Keep the script running to handle the call
    input("Press enter to disable the phone")
    phone.stop()
