import fitdecode
import re


def filter_fitfile(fit_file):
    with fitdecode.FitReader(fit_file) as file:
        filtered_frames = list(
            filter(
                lambda x: isinstance(x, fitdecode.records.FitDataMessage)
                and x.name in ["record", "lap", "workout_step"],
                file,
            )
        )
        return filtered_frames


def convert_frames(filtered_frames, frame_name):
    frame_list = []
    frames = list(filter(lambda x: x.name == frame_name, filtered_frames))
    for frame in frames:
        row_dict = {}
        for field in frame.fields:
            if not field.name.startswith("unknown"):
                if bool(re.search(r"_lat|_long", field.name)):
                    row_dict[field.name] = frame.get_value(field.name) / (
                        (2**32) / 360
                    )
                else:
                    row_dict[field.name] = frame.get_value(field.name)
        frame_list.append(row_dict)
    return frame_list
