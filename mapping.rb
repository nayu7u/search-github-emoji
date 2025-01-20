require "json"
require "uri"

json = JSON.load_file("_data.json")

maps = json.select {  |key, value| value.include? "unicode" }
           .map { |key, value| [key, URI.parse(value).path.split("/").last.split(".").first] }.to_h

File.write("mapping.json", JSON.dump(maps))