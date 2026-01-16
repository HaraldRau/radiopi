def sender(id):
  sender = [
    ["CA 1","http://sc2.radiocaroline.net:10558/"],
    ["nO 2","http://streams.norawebstreams.de/nora-oldies/mp3-192/"],
    ["SA 3","http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa"],
    ["br 4","https://icecast.radiobremen.de/rb/bremeneins/live/mp3/128/stream.mp3"],
    ["H7 5","http://stream.laut.fm/1-hits70s"],
    ["OL 6","https://stream.laut.fm/oldies"],
    ["GO 7","http://stream.laut.fm/the-beat-goes-on"],
    ["SO 8","http://stream.laut.fm/northernsoul"]
  ]
  if id >= len(sender):
    id = len(sender)-1
  return sender[id]
