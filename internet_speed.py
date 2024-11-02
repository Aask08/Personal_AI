import speedtest
from core_utils import speak


def check_internet_speed():
    """Check and report the internet download and upload speeds."""
    try:
        st = speedtest.Speedtest()

        # Get download and upload speeds in Mbps
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        # Format and announce the result
        speed_report = (
            f"Download speed is {download_speed:.1f} Mbps, "
            f"and upload speed is {upload_speed:.1f} Mbps."
        )
        print(speed_report)
        speak(speed_report)

    except Exception as e:
        error_message = "An error occurred while checking the internet speed."
        print(f"{error_message} Error: {e}")
        speak(error_message)
