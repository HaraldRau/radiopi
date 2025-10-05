def sender(id):
  sender = [
    ["Radio Caroline","http://sc2.radiocaroline.net:10558/"],
    ["Radio Nora","http://streams.norawebstreams.de/nora-oldies/mp3-192/"],
    ["RSA Oldies","http://streams.rsa-sachsen.de/rsa-oldies/mp3-192/mediaplayerrsa"],
    ["Radio Bremen","https://d131.rndfnk.com/ard/rb/bremeneins/live/mp3/128/stream.mp3?aggregator=radiolisten-de&cid=01FC1W5AX0V19NKBFPPE0A91GX&sid=33eco5Bcr07LSoVoP6QyJ9AzasK&token=tvOF2emYCvTTCiCzXKER6a51v_bQ8cBzMCz2_CbnAIk&tvf=4jqux1O4axhkMTMxLnJuZGZuay5jb20"],
    ["Hits 70s","http://stream.laut.fm/1-hits70s"],
    ["Our Generation","https://stream.laut.fm/oldies"],
    ["Beat Goes on","http://stream.laut.fm/the-beat-goes-on"],
    ["Northern Soul","http://stream.laut.fm/northernsoul"]
  ]
  if id >= len(sender):
    id = len(sender)-1
  return sender[id]
