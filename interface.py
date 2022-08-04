from typing import Optional

from .genius_api import GeniusApi
from utils.models import ManualEnum, ModuleInformation, ModuleController, ModuleModes, TrackInfo, LyricsInfo, \
    SearchResult, DownloadTypeEnum

module_information = ModuleInformation(
    service_name='Genius',
    module_supported_modes=ModuleModes.lyrics,
    login_behaviour=ManualEnum.manual
)


class ModuleInterface:
    def __init__(self, module_controller: ModuleController):
        self.genius = GeniusApi()
        self.exception = module_controller.module_error

    def search(self, query_type: DownloadTypeEnum, query: str, track_info: TrackInfo = None):
        track_id = None

        if track_info:
            # search by track name
            search_results = self.genius.get_search(f'{track_info.artists[0]} {track_info.name}')

            for result_data in search_results:
                result = result_data.get('result')
                # check if the artist and track name match, ignoring the case
                # TODO: check if that is enough, or if the full track name should be checked
                if (track_info.name.casefold() in result.get('title').casefold() or
                    track_info.name.casefold() in result.get('title_with_featured').casefold()) \
                        and track_info.artists[0].casefold() in result.get('artist_names').casefold():
                    track_id = result.get('id')
                    break

        if track_id:
            return [SearchResult(result_id=track_id)]
        return []

    def get_track_lyrics(self, track_id: str) -> Optional[LyricsInfo]:
        track_data = self.genius.get_song_by_id(track_id)

        return LyricsInfo(
            embedded=track_data.get('lyrics').get('plain') if track_data.get('lyrics') else None,
            synced=None
        )
