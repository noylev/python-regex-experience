import fileinput
import sys
import re

lyrics = """How many roads must a man walk down
Before you can call him a man?
How many seas must a white dove sail
Before she sleeps in the sand?
Yes, how many times must the cannon balls fly
Before they're forever banned?
The answer my friend is blowin' in the wind
The answer is blowin' in the wind.

Yes, how many years can a mountain exist
Before it's washed to the sea?
Yes, how many years can some people exist
Before they're allowed to be free?
Yes, how many times can a man turn his head
Pretending he just doesn't see?
The answer my friend is blowin' in the wind
The answer is blowin' in the wind.

Yes, how many times must a man look up
Before he can really see the sky?
Yes, how many ears must one man have
Before he can hear people cry?
Yes, how many deaths will it take till he knows
That too many people have died?
The answer my friend is blowin' in the wind
The answer is blowin' in the wind."""

pattern = r'How many([\w*\s*]*).*\?'


if re.match(pattern, lyrics):
  print("Match!")
else: print("Not a match!")


if (sys.argv[1] == "regexp"):		
	print(re.sub(pattern,r'\1', lyrics,0,re.M|re.I))
	
		
elif (sys.argv[1] == "pos"):
	print("pos option")


