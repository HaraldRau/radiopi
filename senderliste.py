def sender(id):
  sender = [
    ["RC01","http://sc2.radiocaroline.net:10558/"],
    ["RN02","http://streams.norawebstreams.de/nora-oldies/mp3-192/"],
    ["RO03","http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa"],
    ["RB04","https://icecast.radiobremen.de/rb/bremeneins/live/mp3/128/stream.mp3"],
    ["H705","http://stream.laut.fm/1-hits70s"],
    ["OG06","https://stream.laut.fm/oldies"],
    ["BG07","http://stream.laut.fm/the-beat-goes-on"],
    ["NS08","http://stream.laut.fm/northernsoul"]
  ]
  if id >= len(sender):
    id = len(sender)-1
  return sender[id]
