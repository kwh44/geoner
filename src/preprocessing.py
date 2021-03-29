import html2text


def text_from_html(data_folder_html_file_id):
    road_trip = open("../data/" + str(data_folder_html_file_id) + ".html", "r").read()
    road_trip_processed = html2text.html2text(road_trip)
    for i in ["https://www.nationalgeographic.com/travel \"Travel\""]:
        index = road_trip_processed.find(i)
        road_trip_processed = road_trip_processed[index + len(i) + 1:]
    for i in ["\n", "[", "]", "-", "*", "#", "_"]:
        road_trip_processed = road_trip_processed.replace(i, " ")
    for i in range(4): # 4 seems enough
        road_trip_processed = road_trip_processed.replace("  ", " ")
    return road_trip_processed.strip()
