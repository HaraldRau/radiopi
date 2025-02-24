def sender(id):
  sender = [
    ["Radio Caroline","http://sc2.radiocaroline.net:10558/"],
    ["Radio Nora","http://streams.norawebstreams.de/nora-oldies/mp3-192/"],
    ["RSA Oldies","http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa"],
    ["Hits 70s","http://stream.laut.fm/1-hits70s"],
    ["Our Generation","https://stream.laut.fm/oldies"],
    ["Beat Goes on","http://stream.laut.fm/the-beat-goes-on"],
    ["Northern Soul","http://stream.laut.fm/northernsoul"]
  ]
  if id >= len(sender):
    id = len(sender)-1
  return sender[id]
