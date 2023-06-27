# The Funny Insult Generator
# Always fun to lighten the mood by reading what random terms it generates
# Try here or check the code below https://replit.com/@chetanamrao/TheInsultGenerator
import random
adj1=[
'atomic',
'steamy',
'rusty',
'witless',
'shitty',
'chunky',
'losy',
'bulbous',
'trashy',
'dumbass',
'lumpy',
'crusty',
'brainless']

main = [
'knob',
'bum',
'turd',
'prick',
'ass',
'shit',
'rod',
'fuck',
'weiner',
'jizz',
'cock',
'bulge',
'dong'
]

end = [
  'vaccum',
  'pixie',
  'gremlin',
  'spasm',
  'tunnel',
  'fungus',
  'corporal',
  'raider',
  'buccaneer',
  'tyrant',
  'juggler',
  'hound',
  'fiddle'
]

print(random.choice(adj1)+' '+random.choice(main)+ ' '+random.choice(end))
