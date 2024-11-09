def sender(id):
  sender = [
    ["Radio Caroline","http://sc2.radiocaroline.net:10558/"],
    ["Radio Nora","http://streams.norawebstreams.de/nora-oldies/mp3-192/"],
    ["Berliner Rundfunk","https://topradio-stream31.radiohost.de/brf-60er-70er_mp3-192?_art=dD0xNzMxMTYxMTM3JmQ9NGU0NmNiOGZjNjc5ZjJiNjhlMWM"],
    ["RSA Beatles","http://streams.rsa-sachsen.de/rsa-beatles/mp3-192/mediaplayerrsa"],
    ["RSA Oldies","http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa"],
    ["Jukebox Hits","https://stream.laut.fm/50s60s-radio"],
    ["Hits 70s","http://stream.laut.fm/1-hits70s"],
    ["Radio 70","https://stream.laut.fm/radio70"],
    ["Our Generation","https://stream.laut.fm/oldies"],
    ["Beat Goes on","http://stream.laut.fm/the-beat-goes-on"],
    ["Northern Soul","http://stream.laut.fm/northernsoul"]
  ]
  if id >= len(sender):
    id = len(sender)-1
  return sender[id]
