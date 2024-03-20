from transformers import pipeline
nlp = pipeline(task='text-classification', 
               model='nickwong64/bert-base-uncased-poems-sentiment')
p1 = """
I wanna know who mothafuckin' representin' in here tonight
Hold on, hold on
I keep lettin' you back in (You back in)
How can I, explain myself?
Care for me, care for me, you said you'd care for me
There for me, there for me, said you'd be there for me
(Lil Weezyana shit)
Cry for me, cry for me, you said you'd die for me
(Murda on the beat)
Give to me, give to me, why won't you live for me?
Care for me, care for me, I know you care for me
(A song for y'all to cut up to, you know?)
There for me, there for me, said you'd be there for me (Yeah)
Cry for me, cry for me, you said you'd die for me
Give to me, give to me, why won't you live for me?
Everybody get your mothafuckin' roll on
I know shorty and she doesn't want no slow song
Had a man last year, life goes on
Haven't let that thing loose, girl, in so long
You've been inside, know you like to lay low
I've been peepin' what you bringin' to the table
Workin' hard, girl, everything paid for
First-last, phone bill, car note, cable
With your phone out, gotta hit them angles
With your phone out, snappin' like you Fabo
And you showin' off, but it's alright
And you showin' off, but it's alright (Alright!)
It's a short life, yeah
Care for me, care for me, you said you'd care for me
There for me, there for me, said you'd be there for me
Cry for me, cry for me, you said you'd die for me
Give to me, give to me, why won't you live for me?
That's a real one in your reflection
Without a follow, without a mention
You really pipin' up on these niggas
You gotta be nice for what to these niggas?
I understand, you got a hunnid bands
You got a baby Benz, you got some bad friends
High school pics, you was even bad then
You ain't stressin' off no lover in the past tense
You already had them
Work at 8 a.m., finish 'round five
Hoes talk down, you don't see 'em outside
Yeah, they don't really be the same offline
You know dark days, you know hard times
Doin' overtime for the last month
Saturday, call the girls, get 'em gassed up
Gotta hit the club, gotta make that ass jump
Gotta hit the club like you hit them mothafuckin' angles
With your phone out, snappin' like you Fabo
And you showin' off, but it's alright
And you showin' off, but it's alright (Alright!)
It's a short life
Uh-huh! (Oh yeah!)
These hoes! (They mad!)
Your boy! (I had!)
I made! (Watch the breakdown)
Care for me, care for me, you said you'd care for me
There for me, there for me, said you'd be there for me
Cry for me, cry for me, you said you'd die for me
Give to me, give to me, why won't you live for me?
Gotta make that jump, gotta make that, gotta, gotta make that
Gotta make that jump, gotta make that, gotta, gotta make that
Gotta, gotta, gotta g-g-gotta, g-g-gotta, gotta
Gotta, g-g-gotta, gotta, gotta make that jump, jump (Let's go)
Bend it over, lift it up, bend it over, lift it up (Make that jump, jump)
Bend it over, lift it up, bend it over, lift it up (Make that jump, jump)
Bend it over, over, over, over, over, lift it up (Make that jump, jump)
Bend it over, lift it up (Make that jump, jump)
Bend it over, lift it up (Make that jump, jump)
That's a real one in your reflection
Without a follow, without a mention
You really pipin' up on these niggas
You gotta be nice for what to these niggas?
I understand
Care for me, care for me, you said you'd care for me
There for me, there for me, said you'd be there for me
Give to me, give to me, why won't you live for me?
Cry for me, cry for me, you said you'd cry for me
Gotta hit the club like you hit them, hit them, hit them angles
It's a short life, yeah
Cry for me, cry for me, you said you'd die for me
Give to me, give to me, why won't you live for me?
"""

print(nlp(p1))
