def main():
    print("Hello from youtube-transcript-curlify!")


if __name__ == "__main__":
    main()

import sys
from curlify2 import Curlify
from youtube_transcript_api import YouTubeTranscriptApi

def main():
    ytt_api = YouTubeTranscriptApi()
    print(ytt_api.list("V_xro1bcAuA"))
#    print(ytt_api.fetch(video_id="V_xro1bcAuA", languages=['en']))
    # print(Curlify(ytt_api.list("V_xro1bcAuA")))


if __name__ == "__main__":
    main()
