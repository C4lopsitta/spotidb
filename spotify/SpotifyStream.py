from datetime import datetime


class SpotifyStream:
    def __init__(self,
                 ts: str,
                 platform: str | None = None,
                 ms_played: int | None = None,
                 conn_country: str | None = None,
                 ip_addr: str | None = None,
                 master_metadata_track_name: str | None = None,
                 master_metadata_album_artist_name: str | None = None,
                 master_metadata_album_album_name: str | None = None,
                 spotify_track_uri: str | None = None,
                 episode_name: str | None = None,
                 episode_show_name: str | None = None,
                 spotify_episode_uri: str | None = None,
                 audiobook_title: str | None = None,
                 audiobook_uri: str | None = None,
                 audiobook_chapter_uri: str | None = None,
                 audiobook_chapter_title: str | None = None,
                 reason_start: str | None = None,
                 reason_end: str | None = None,
                 shuffle: bool | None = None,
                 skipped: bool | None = None,
                 offline: bool | None = None,
                 offline_timestamp: str | None = None,
                 incognito_mode: bool | None = None):
        self.ts = ts
        self.platform = platform
        self.ms_played = ms_played
        self.conn_country = conn_country
        self.ip_addr = ip_addr
        self.master_metadata_track_name = master_metadata_track_name
        self.master_metadata_album_artist_name = master_metadata_album_artist_name
        self.master_metadata_album_album_name = master_metadata_album_album_name
        self.spotify_track_uri = spotify_track_uri
        self.episode_name = episode_name
        self.episode_show_name = episode_show_name
        self.spotify_episode_uri = spotify_episode_uri
        self.audiobook_title = audiobook_title
        self.audiobook_uri = audiobook_uri
        self.audiobook_chapter_uri = audiobook_chapter_uri
        self.audiobook_chapter_title = audiobook_chapter_title
        self.reason_start = reason_start
        self.reason_end = reason_end
        self.shuffle = shuffle
        self.skipped = skipped
        self.offline = offline
        self.offline_timestamp = offline_timestamp
        self.incognito_mode = incognito_mode

    def is_song(self) -> bool:
        return self.episode_name is None and self.audiobook_title is None

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)

    def to_dict(self) -> dict:
        return self.__dict__
    
    def ms_to_time(self) -> str:
        if self.ms_played is None:
            return "00:00"

        total_seconds = self.ms_played // 1000
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return f"{minutes:02d}:{seconds:02d}"

    def get_pctg_streamed(self, track_duration_ms: int) -> float:
        if self.ms_played is None:
            return 0.0
        return (self.ms_played / track_duration_ms) * 100

    def to_ts(self) -> int:
        dt = datetime.fromisoformat(self.ts.replace("Z", "+00:00"))
        return int(dt.timestamp())

    def to_offline_timestamp(self) -> int:
        if self.offline_timestamp is None:
            return 0
        if type(self.offline_timestamp) is not str:
            return int(self.offline_timestamp)
        dt = datetime.fromisoformat(self.offline_timestamp.replace("Z", "+00:00"))
        return int(dt.timestamp())

    def __str__(self):
        return f"{self.ts} - {self.master_metadata_track_name} - {self.master_metadata_album_artist_name} - {self.reason_start} - {self.ms_to_time()} - {self.reason_end}"

###   --== SCHEMA == -- ###
# {
#     "ts": "2021-02-12T06:14:19Z",
#     "platform": "Android OS 11 API 30 (samsung, SM-G975F)",
##     "ms_played": 10036,
#     "conn_country": "IT",
##     "ip_addr": "151.46.60.9",
##     "master_metadata_track_name": null,
##     "master_metadata_album_artist_name": null,
3#     "master_metadata_album_album_name": null,
##     "spotify_track_uri": null,
#     "episode_name": "#1609 - Elon Musk",
#     "episode_show_name": "The Joe Rogan Experience",
#     "spotify_episode_uri": "spotify:episode:2aB2swgyXqbFA06AxPlFmr",
#     "audiobook_title": null,
#     "audiobook_uri": null,
#     "audiobook_chapter_uri": null,
#     "audiobook_chapter_title": null,
##     "reason_start": "playbtn",
##     "reason_end": "endplay",
##     "shuffle": false,
##     "skipped": false,
##     "offline": false,
##     "offline_timestamp": null,
##     "incognito_mode": false
#   },
