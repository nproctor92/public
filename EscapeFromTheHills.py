# improvement notes - different description when you have been to a place in the reference to that place
loc = [1, 1]
inv = []
part2 = ""
knot = 1
cleared12 = 0
truckfilled = 0
oldmancount = 0
oldman = {
    0: 'The old man takes a long pull from an open jug, squints at you, and says "Nothing like some good ol\' homemade.\
Try getting that flavor from one of your fancy state liquor stores." He says "state liquor stores" in the same tone of \
voice you might use to say "festering tapeworm."',
    1: 'The old man pokes at the logs with his stick for a bit, eventually eliciting a low flame. Leaning back into his\
 chair, he says "Back in my day, if you wanted to run an engine on anything other than pump gas, you\'d have to re-grin\
d the carb. Now, the computer on some of these things can run it on basically any liquid that explodes."',
    2: 'A leaf drops from a nearby tree. The man rapidly puts the jug to his mouth and begins drinking, following the f\
light of the leaf with his eyes. When the leaf hits the ground, he stops and wipes his mouth. After a contented sigh, h\
e says "You ever notice how all the big cities are on water? It\'s like, if you follow any river for long enough, event\
ually you\'ll find people.',
    3: 'The old man drains the last of the current jug and places it behind him, then picks up another jug and twists t\
he cap off. He takes a long swallow and says "Quality control testing, very important."'
}

inpconvert = {
    "inner tube": "inner tube",
    "tire swing": "inner tube",
    "tire": "inner tube",
    "tube": "inner tube",
    "inflated inner tube": "inner tube",
    "moonshine": "moonshine",
    "alcohol": "moonshine",
    "booze": "moonshine",
    "vodka": "moonshine",
    "jug of moonshine": "moonshine",
    "knife": "knife",
    "key": "key",
    "keys": "key",
    "keyring": "key",
    "ring of keys": "key",
    "truck key": "key",
    "coat": "coat",
    "hoodie": "coat",
    "overcoat": "coat",
    "sweater": "coat",
    "rifle": "rifle",
    "baker rifle": "rifle",
    "musket": "rifle",
    "muzzleloader": "rifle",
    "flintlock": "rifle",
    "gun": "rifle",
    "truck": "truck",
    "pickup": "truck",
    "pickup truck": "truck",
    "ford": "truck",
    "rope": "rope",
    "knot": "knot",
    "tube rope": "rope",
    "powder": "powder",
    "gunpowder": "powder",
    "powder trail": "powder",
    "gunpowder trail": "powder",
    "river": "river",
    "water": "river",
    "creek": "river"
}

inpkeys = list(inpconvert.keys())

locinter = {
    "21": ["truck"],
    "31": ["rope", "river"],
    "32": ["moonshine", "river"],
    "12": ["powder"],
    "33": ["river"]
}
locitems = {
    "31": ["inner tube"],
    "13": ["moonshine"],
    "112": ["knife"],
    "122": ["key", "coat"],
    "133": ["rifle"]
}
locitkeys = list(locitems.keys())
eastout = "To the East is a wide, smooth, deep, and fast-moving river."
southout = "To the South is a dense forest that, despite the brightness of the midday sun, is already shrouded in dark\
ness."
northout = "To the North is a dense forest that, despite the brightness of the midday sun, is already shrouded in dark\
ness."
westout = "To the West is an empty and winding road. It is miles to the nearest other driveway, let alone the nearest \
gas station or convenience store."
locdesc = {
    "11": f"You find yourself in the Southwest corner of a flat clearing. Around you is a turnaround \
area at the top of the driveway. To the North is a barn. To the East is a car port with a couple of vehicles under it. \
{westout} {southout}",
    "12": f"Standing stark against the horizon is a squat, sturdy barn with peeling white paint and a lightly-corroded \
tin roof. ",
    "13": f"In a shed sits a still consisting of several copper containers connected by metal tubing dripping mer\
rily away. You now know what snorting hand sanitizer would smell and feel like. A shelf lined with empty gallon jugs \
stands to the right of the receiving flask. ",
    "21": f"You are outside a car port with two vehicles in it. One is an 80's Oldsmobile on blocks. The other is a For\
d pickup truck with a FlexFuel badge on the tailgate. It looks clean and well-maintained. To the East is a tree with a \
tree swing. To the West is the turnaround area at the top of the driveway. To the north is a double-wide. {southout}",
    "22": 'You are standing in front of a worn, but apparently structurally sound double-wide trailer. Its color is \
faded like a cheap shirt that has been through the wash too many times. The skirting around the bottom is intact, exce\
pt for one area where an arch about a foot high has been cut out beneath a sign with "Dale" crudely written on it. \
\n \n There is no sign of Dale. \n \n There\
 is a set of stairs leading up to the door made out of stacked cinder blocks. To the West is a barn. To the East is \
a campfire surrounded by chairs. To the South is a car port with a couple of vehicles under it. To the North is a ra\
nge.',
    "23": f"In front of you is a roof supported by four posts. Sheltered by the roof is a table with a stool. It could \
almost be mistaken for a picnic spot, if the view from the stool wasn't of an assortment of targets, shards of glass,\
 thoroughly-holed cans, \
and a stack of railroad ties backed by a tall mound of well-packed dirt. To the West is a still. To the East is a tree \
with a small house nestled in the branches. To the South is a double-wide. {northout}",
    "31": f"A tall, broad, oak tree stands near the river. Its leaves rustle gently in the faint breeze, creating shift\
ing but generous patterns of shade along the shoreline. ",
    "32": f'You come across a campfire surrounded by approximately evenly-spaced chairs. One of these contains a heavil\
y-bearded old man with a round face bearing more broken veins than a remedial phlebotomist class. His heavily-lidded ey\
es are unfocused, his faded "Ron Paul \'08" t-shirt is stained, and his jeans came by their fashionable knee-rips hones\
tly. In his right hand is a long, straight, stick whose burnt end is resting on the rocks marking the outer ring of the\
 fire pit. Around him is scattered a handful of gallon jugs, which were filled to seemingly random levels. The fire is \
crackling merrily. To the South is a tree with a tree swing. To the North is a tree with a small h\
ouse nestled in the branches. To the West is a double-wide. {eastout}',
    "33": f"Standing alone in a meadow is a tall tree with a small house nestled in the branches. A series of boards na\
iled to the trunk serves as a ladder. The meadow is a mixture of shin-high grass, fluffy purple clovers, and dandelions\
. To the West is a range. To the South is a campfire surrounded by chairs. {eastout} {northout}",
    "00": "While driving down a winding mountain road in rural West Virginia, you see a deer burst out in front of \
your car. You yank on the wheel and slam on the brakes, but don't have time to avoid it. The impact sets off the \
airbags. As the deer passes under your vehicle, you hear a dull 'thunk,' followed by the sound of liquid splattering on\
 the pavement and the smell of gasoline. You can only remember seeing one mailbox in the last 20 miles, so you reluctan\
tly head back to it and trudge up the driveway in search of assistance. You must find some way of getting back to \
town. \n \n ",
    "112": f"Light filters through the gaps in the boards, highlighting suspended motes of dust. Against one wall is a \
table with a lathe",
    "122": f"You are in a low-ceilinged living room furnished with mismatched but comfortable furniture. An old-school \
CRT sits on a cabinet opposite the sofa. Above the TV hangs a board holding a katana and a wakizashi in their tasseled \
scabbards. The faint whiff of approximately 300 cigarettes hangs in the air. ",
    "133": f"You are in a small, square, wooden structure at the first substantial fork in the tree. There are large op\
enings cut into the sides that serve as windows. "
}


def conlinre(text):
    length = 75
    work = text.split(" ")
    out = ""
    count = 0
    for i in work:
        count += len(i) + 1
        if count <= length + 1 and i == "\n":
            out += i
            count = 0
        elif count <= length + 1:
            out += i + " "
        else:
            out += "\n" + i + " "
            count = len(i) + 1
    return out


def interpret():
    command = input("\nEnter next move\n>")
    command = command.lower()
    work = command.split(" ")
    global yank
    global cleared12
    global loc
    global lockey
    global locstr
    global counter
    global victory
    global inv
    global oldmancount
    global knot
    global truckfilled
    global locact
    global locitkeys
    if work[0] == "go":
        if (work[1] == "north" or work[1] == "forward") and (loc != [11, 2] and loc != [12, 2] and loc != [13, 3]):
            if loc[1] + 1 <= 3:
                counter = 0
                loc[1] = loc[1] + 1
            else:
                x = f"You stride confidently into the thick forest, whistling a jaunty tune. \
After 20 minutes of forging arduously ahead, you see a clearing in the distance. \
You move towards it as fast as you can, bursting into the light, where you find yourself exactly where you started."
                print(conlinre(x))
        elif (work[1] == "south" or work[1] == "back") and (loc != [11, 2] and loc != [12, 2] and loc != [13, 3]):
            if loc[1] - 1 >= 1:
                counter = 0
                loc[1] = loc[1] - 1
            else:
                x = f"You stride confidently into the thick forest, whistling a jaunty tune. \
After 20 minutes of forging arduously ahead, you see a clearing in the distance. \
You move towards it as fast as you can, bursting into the light, where you find yourself exactly where you started."
                print(conlinre(x))
        elif (work[1] == "east" or work[1] == "right") and (loc != [11, 2] and loc != [12, 2] and loc != [13, 3]):
            if loc[0] + 1 <= 3:
                counter = 0
                loc[0] = loc[0] + 1
            else:
                x = "The river, while not turbulent, is far too fast and deep to swim or wade in \
without a flotation device."
                print(conlinre(x))
        elif (work[1] == "west" or work[1] == "left") and (loc != [11, 2] and loc != [12, 2] and loc != [13, 3]):
            if loc[0] - 1 >= 1:
                counter = 0
                loc[0] = loc[0] - 1
            else:
                x = "The road is completely deserted. You currently have no means of transportation."
                print(conlinre(x))
        elif work[1] == "up":
            if loc == [3, 3]:
                counter = 0
                loc[0] = loc[0] + 10
            else:
                print("There is nothing to climb.")
        elif work[1] == "down":
            if loc == [13, 3]:
                counter = 0
                loc[0] = loc[0] - 10
            else:
                print("There is nothing to climb down.")
        elif work[1] == "in":
            if (loc == [1, 2] and cleared12 == 1) or loc == [2, 2]:
                counter = 0
                loc[0] = loc[0] + 10
            else:
                print("There is nothing to enter.")
        elif work[1] == "out":
            if loc == [11, 2] or loc == [12, 2]:
                counter = 0
                loc[0] = loc[0] - 10
            else:
                print("You are not in anything you can exit.")
        elif work[1] == "northeast" and (loc != [11, 2] and loc != [12, 2] and loc != [13, 3]):
            if loc[0]+1 > 3:
                x = "The river, while not turbulent, is far too fast and deep to swim or wade in \
without a flotation device."
                print(conlinre(x))
            elif loc[1]+1 > 3:
                x = f"You stride confidently into the thick forest, whistling a jaunty tune. \
After 20 minutes of forging arduously ahead, you see a clearing in the distance. \
You move towards it as fast as you can, bursting into the light, where you find yourself exactly where you started."
                print(conlinre(x))
            else:
                counter = 0
                loc = [i+1 for i in loc]
        elif work[1] == "northwest" and (loc != [11, 2] and loc != [12, 2] and loc != [13, 3]):
            if loc[0]-1 < 1:
                x = "The road is completely deserted. You currently have no means of transportation."
                print(conlinre(x))
            elif loc[1]+1 > 3:
                x = f"You stride confidently into the thick forest, whistling a jaunty tune. \
After 20 minutes of forging arduously ahead, you see a clearing in the distance. \
You move towards it as fast as you can, bursting into the light, where you find yourself exactly where you started."
                print(conlinre(x))
            else:
                counter = 0
                loc = [loc[0]-1, loc[1]+1]
        elif work[1] == "southeast" and (loc != [11, 2] and loc != [12, 2] and loc != [13, 3]):
            if loc[0] + 1 > 3:
                x = "The river, while not turbulent, is far too fast and deep to swim or wade in \
without a flotation device."
                print(conlinre(x))
            elif loc[1] - 1 < 1:
                x = f"You stride confidently into the thick forest, whistling a jaunty tune. \
After 20 minutes of forging arduously ahead, you see a clearing in the distance. \
You move towards it as fast as you can, bursting into the light, where you find yourself exactly where you started."
                print(conlinre(x))
            else:
                counter = 0
                loc = [loc[0]+1, loc[1]-1]
        elif work[1] == "southwest" and (loc != [11, 2] and loc != [12, 2] and loc != [13, 3]):
            if loc[0]-1 < 1:
                x = "The road is completely deserted. You currently have no means of transportation."
                print(conlinre(x))
            elif loc[1]-1 < 1:
                x = f"You stride confidently into the thick forest, whistling a jaunty tune. \
After 20 minutes of forging arduously ahead, you see a clearing in the distance. \
You move towards it as fast as you can, bursting into the light, where you find yourself exactly where you started."
                print(conlinre(x))
            else:
                counter = 0
                loc = [loc[0]-1, loc[1]-1]
        else:
            print("Direction not available")
    elif work[0] == "quit" or work[0] == "q":
        victory = "Q"
    elif work[0] == "look":
        print(locstr)
    elif work[0] == "help" or work[0] == "h":
        x = "Your goal is to find some way to travel back to town. Useful commands are: go, take, use, inv, look, help,\
 quit."
        print(conlinre(x))
    elif work[0] == "inv":
        print(inv)
    elif work[0] == "enter":
        if loc == [2, 2] or (loc == [1, 2] and cleared12 == 1):
            counter = 0
            loc[0] = loc[0]+10
        else:
            print("There is nothing to enter")
    elif work[0] == "exit":
        if loc == [12, 2] or loc == [11, 2]:
            counter = 0
            loc[0] = loc[0] - 10
        else:
            print("You are not in anything that you can exit")
    elif work[0] == "take":
        temp = " ".join(work[1:])
        if temp in inpkeys and lockey in locitkeys:
            itconv = inpconvert[temp]
            if loc == [3, 1] and itconv in locitems[lockey]:
                if knot == 1:
                    if yank == 1:
                        x = "You give the inner tube a firm tug. The branch it is tied to does not budge."
                        yank += 1
                    elif yank == 2:
                        x = "You grab the inner tube with both hands and pull as hard as you can, adding yo\
ur body weight to the effort. The knot, if anything, grows even more intractable. The inner tube remains fir\
mly attached to the tree."
                        yank += 1
                    elif yank == 3:
                        x = "You spot a conveniently placed root to brace your feet against, and, after spitting on you\
your hands for traction, bring the inner tube over. You strain as hard as you can, veins bulging and tendons creaking. \
About three Newtons before your abdominal wall opens the door for the traveling hernia salesman, the tire slips out of \
your hands and you fall back hard. The inner tube is still firmly attached to the tree."
                        yank += 1
                    else:
                        x = "You half-heartedly tug on the inner tube. It hangs mockingly."
                    print(conlinre(x))
                else:
                    inv.append(itconv)
                    locitems[lockey].remove(itconv)
                    print(f"You take the {temp}")
                    counter = 0
            elif itconv == "moonshine" and loc == [3, 2]:
                x = "The old man pulls the nearest jug closer to himself and gives you a warning growl."
                print(conlinre(x))
            elif itconv in locitems[lockey]:
                inv.append(itconv)
                locitems[lockey].remove(itconv)
                print(f"You take the {temp}")
                counter = 0
            else:
                print("Item not present.")
        else:
            print(f"{temp} cannot be taken.")
    elif work[0] == "talk":
        if loc == [3, 2]:
            if len(work) == 1:
                num = oldmancount%4
                x = oldman[num]
                oldmancount += 1
            elif work[1] == "old" or work[1] == "man":
                num = oldmancount%4
                x = oldman[num]
                oldmancount += 1
            else:
                x = "After a few words, you notice the old man giving you a perplexed and slightly worried look."
            print(conlinre(x))
        elif loc == [12, 2]:
            x = "Midway through your first sentence, you hear an electronic chime followed by a feminine robot voice sa\
ying: \"Sorry, I didn't quite catch that.\" You lapse sheepishly into silence."
            print(conlinre(x))
        else:
            if len(work) == 1 or work[1] == "self":
                x = "You have a very pleasant conversation with yourself. You find you agree on a lot."
            else:
                x = "You hear no response"
            print(conlinre(x))
    elif work[0] == "use":
        if len(work) == 1:
            x = "You can't use here, this is a terrible place to nod off and you left your stash in the car anyway."
            print(conlinre(x))
        elif "with" in work or "on" in work:
            temp = " ".join(work[1:])
            if "on" in work: temp = temp.split(" on ")
            if "with" in work: temp = temp.split(" with ")
            head = temp[0]
            tail = temp[1]
            if head in inpkeys and tail in inpkeys:
                head = inpconvert[head]
                tail = inpconvert[tail]
                if head not in inv or tail not in locact:
                    print("Combination not possible")
                elif head == "knife" and tail == "rope":
                    x = "Holding the rope taught with your left hand, you begin sawing at it with your ri\
ght. The fibers part rapidly as the blade slides back and forth. Soon, the last strands holding the rope together tear,\
and the inner tube drops to the ground."
                    print(conlinre(x))
                    knot = 0
                    counter = 0
                elif head == "rifle" and tail == "powder":
                    x = "You place the flintlock on its side so that the mechanism is as close to the end of th\
e powder trail as possible, then carefully cock it. Taking a deep breath, you pull the trigger. and step back. A shower\
 of sparks hits the powder trail, igniting it. A bright flame sputters and smokes its way along the trail, leaving a tr\
ail of scorched grass in its wake. It reaches the cask and disappears. A heartbeat later, the cask and sacks of flour d\
isappear with a bright flash and a dull boom that presses painfully on your eardrums."
                    print(conlinre(x))
                    locinter["12"] = []
                    cleared12 = 1
                    counter = 0
                elif head == "moonshine" and tail == "truck":
                    x = "You head over to the Ford and pop open the flap covering the truck's fill tube. After \
carefully pulling out the stopper, you push the mouth of the bottle into the fill tube and upend it, emptying the whole\
 gallon of moonshine into the tank, then toss the empty jug into the corner."
                    truckfilled = 1
                    inv.remove("moonshine")
                    print(conlinre(x))
                elif head == "key" and tail == "truck" and truckfilled == 0:
                    x = "You unlock the door, open it, and clamber inside. Putting the key in the ignition and turning \
it yields only the sound of the engine cranking; it is clearly not even close to turning over. The problem jumps out at\
 you after a quick glance at the dashboard: the gas gauge is buried firmly at the bottom of \"E.\" This truck isn't goi\
ng anywhere until it has fuel."
                    print(conlinre(x))
                elif head == "key" and tail == "truck" and truckfilled == 1:
                    x = "You unlock the door, open it, and clamber inside. You put the key in the ignition and \
give it a hopeful twist. After a second of cranking, the engine fires up and settles into a rough idle. Not willing to \
waste even a second, you immediately throw it into gear and surge out of the car port. Barely even slowing down at the \
foot of the driveway, you make a sharp left and head back towards town."
                    print(conlinre(x))
                    victory = "Y"
                elif head == "inner tube" and tail == "river":
                    x = "You carry the inner tube over to the river bank and wade a few steps in. The water is \
lukewarm. Bending over to ensure your center of gravity is over the middle of the inner tube, you step deeper into the \
river. The current pulls at your legs. Right as your feet start to lose contact with the ground, you use them for one f\
inal push and drift out towards the center of the river where the current is swiftest. As the clearing slides away behi\
nd you, you give it one last wave of farewell."
                    print(conlinre(x))
                    victory = "Y"
                else:
                    print("This will not accomplish anything.")
            else:
                print("Item(s) not recognized.")
        else:
            back = " ".join(work[1:])
            if back in inpkeys:
                temp = inpconvert[back]
                if temp in inv or temp in locact:
                    if temp == "rifle":
                        if loc == [1, 3]:
                            x = "You shoulder the flintlock, cock it, take careful aim, and pull the trigger. The spar\
ks from the flint hitting the frizzen immediately ignite the moonshine in the air. The last thing you see is a rapidly \
expanding ball of fire."
                            print(conlinre(x))
                            victory = "X"
                        elif loc == [1, 2] and cleared12 == 0:
                            x = "You place the flintlock on its side so that the mechanism is as close to the end of th\
e powder trail as possible, then carefully cock it. Taking a deep breath, you pull the trigger. and step back. A shower\
 of sparks hits the powder trail, igniting it. A bright flame sputters and smokes its way along the trail, leaving a tr\
ail of scorched grass in its wake. It reaches the cask and disappears. A heartbeat later, the cask and sacks of flour d\
isappear in a bright flash and a dull boom that presses painfully on your eardrums."
                            print(conlinre(x))
                            locinter["12"] = []
                            cleared12 = 1
                            counter = 0
                        else:
                            x = "You shoulder the flintlock, cock it, take careful aim, and pull the trigger. The flint\
hitting the frizzen produces a flash of sparks, but because it's not loaded, nothing else happens."
                            print(conlinre(x))
                    elif temp == "knife":
                        if loc == [3, 1] and knot == 1:
                            x = "Holding the rope taught with your left hand, you begin sawing at it with your ri\
ght. The fibers part rapidly as the blade slides back and forth. Soon, the last strands holding the rope together tear,\
 and the inner tube drops to the ground."
                            print(conlinre(x))
                            knot = 0
                            counter = 0
                        elif loc == [3,2]:
                            x = "The old man gives you a stern look and says \"I wouldn't try that if I were you.\" Yo\
u elect to take his advice."
                            print(conlinre(x))
                        else:
                            x = "You do not see anything that it would help you to cut."
                            print(conlinre(x))
                    elif temp == "moonshine":
                        if loc == [2, 1] and truckfilled == 0:
                            x = "You head over to the Ford and pop open the flap covering the truck's fill tube. After \
carefully pulling out the stopper, you push the mouth of the bottle into the fill tube and upend it, emptying the whole\
 gallon of moonshine into the tank, then toss the empty jug into the corner."
                            truckfilled = 1
                            inv.remove("moonshine")
                            print(conlinre(x))
                        else:
                            x = "You swallow a few mouthfuls of 'shine. It burns fiercely going down, and tears stream \
from your eyes as you briefly double over. Almost immediately, you feel dizzy, and sit down for a while to enjoy the sc\
enery spinning around you."
                            print(conlinre(x))
                    elif temp == "key":
                        if loc == [2, 1] and truckfilled == 0:
                            x = "You unlock the door, open it, and clamber inside. Putting the key in th\
e ignition and turning it yields \
only the sound of the engine cranking; it is clearly not even close to turning over. The problem jumps out at you after\
 a quick glance at the dashboard: the gas gauge is buried firmly at the bottom of \"E.\" This truck isn't going anywh\
ere until it has fuel."
                            print(conlinre(x))
                        elif loc == [2, 1] and truckfilled == 1:
                            x = "You unlock the door, open it, and clamber inside. You put the key in the ignition and \
give it a hopeful twist. After a second of cranking, the engine fires up and settles into a rough idle. Not willing to \
waste even a second, you immediately throw it into gear and surge out of the car port. Barely even slowing down at the \
foot of the driveway, you make a sharp left and head back towards town."
                            print(conlinre(x))
                            victory = "Y"
                        else:
                            x = "There is nothing productive you can use the key for here."
                            print(conlinre(x))
                    elif temp == "inner tube":
                        if loc[0] == 3:
                            x = "You carry the inner tube over to the river bank and wade a few steps in. The water is \
lukewarm. Bending over to ensure your center of gravity is over the middle of the inner tube, you step deeper into the \
river. The current pulls at your legs. Right as your feet start to lose contact with the ground, you use them for one f\
inal push and drift out towards the center of the river where the current is swiftest. As the clearing slides away behi\
nd you, you give it one last wave of farewell."
                            print(conlinre(x))
                            victory = "Y"
                        else:
                            x = "There is no way to use that here."
                            print(conlinre(x))
                    elif temp == "coat":
                        x = "You put on the coat. It is very comfortable."
                        inv.remove("coat")
                        print(conlinre(x))
                    elif temp == "truck":
                        if truckfilled == 1 and "key" in inv:
                            x = "You unlock the door, open it, and clamber inside. You put the key in the ignition and \
give it a hopeful twist. After a second of cranking, the engine fires up and settles into a \
rough idle. Not willing to waste even a second, you immediately throw it into gear and surge out of the car port. Bare\
ly even slowing down at the foot of the driveway, you make a sharp left and head back towards town."
                            print(conlinre(x))
                            victory = "Y"
                        elif truckfilled == 0 and "key" in inv:
                            x = "You unlock the door, open it, and clamber inside. Putting the key in the ignition and \
turning it yields only the sound of the engine cranking; it is clearly not even close to turning over. The problem jump\
s out at you after a quick glance at the dashboard: the gas gauge is buried firmly at the bottom of \"E.\" This truck i\
sn't going anywhere until it has fuel."
                            print(conlinre(x))
                        else:
                            x = "The truck door is firmly locked. You would need a key to unlock it."
                            print(conlinre(x))
                    else:
                        print("Nothing happens.")
                else:
                    print("item not available.")
            else:
                print("item not recognized")
    else:
        print("command not recognized")


victory = "N"


def game():
    global loc
    global victory
    global lockey
    global locstr
    global counter
    global cleared12
    global part2
    global yank
    global northout
    global southout
    global eastout
    global westout
    global locact
    global locstuff
    print(conlinre(locdesc["00"]))
    input("press ENTER to continue")
    counter = 0
    yank = 1
    while victory == "N":
        match loc:
            case [1, 1]:
                locstuff = []
                locact = []
                lockey = "".join([str(i) for i in loc])
                locstrtemp = locdesc[lockey]
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [1, 2]:
                locstuff = []
                if cleared12 == 0:
                    part2 = f"The sliding doors to the barn are blocked by a by a couple of sacks of flour. Nestled in \
between the sacks of flower is a small cask filled with gunpowder. A trail of powder leads a safe distance away. To the\
 North is a still. To the East is a double-wide. To the South is a turnaround area at the top of the driveway. \
{westout}"
                else:
                    part2 = f"A small crater smokes gently away in front of the door frame. The sliding doors hang limp\
ly at an angle. Through the gap in the doors, you see what look like stacks of crates. To the North is a still. To the \
East is a double-wide. To the South is a turnaround area at the top of the driveway. {westout}"
                lockey = "".join([str(i) for i in loc])
                locact = locinter[lockey]
                locstrtemp = locdesc[lockey] + part2
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [1, 3]:
                locact = []
                lockey = "".join([str(i) for i in loc])
                locstuff = locitems[lockey]
                if len(locstuff) == 1:
                    part2 = f"A fresh gallon jug of moonshine sits in front of the shelves. The glass is thick and clea\
r. A stopper prevents the moonshine from spilling. To the East is a range. To the South is a barn. {northout} {westout}"
                else:
                    part2 = f"To the East is a range. To the South is a barn. {northout} {westout}"
                locstrtemp = locdesc[lockey] + part2
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [2, 1]:
                locstuff = []
                lockey = "".join([str(i) for i in loc])
                locact = locinter[lockey]
                locstrtemp = locdesc[lockey]
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [2, 2]:
                locstuff = []
                locact = []
                lockey = "".join([str(i) for i in loc])
                locstrtemp = locdesc[lockey]
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [2, 3]:
                locstuff = []
                locact = []
                lockey = "".join([str(i) for i in loc])
                locstrtemp = locdesc[lockey]
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [3, 1]:
                lockey = "".join([str(i) for i in loc])
                locstuff = locitems[lockey]
                locact = locinter[lockey]
                if len(locstuff) == 1 and knot == 1:
                    part2 = f"A thick branch juts from a point about 15 feet up the tree trunk. Hanging from the branch,\
 at the perfect height to serve as a swing, is an inflated inner tube. The rope attaching it to the branch is an inch t\
hick and tied with an absurdly complicated and tight knot that you have absolutely no hope of untying. To the North is \
a campfire surrounded by chairs. To the West is a carport with a couple of cars under it. {southout} {eastout}"
                elif len(locstuff) == 1 and knot == 0:
                    part2 = f"A thick branch juts from a point about 15 feet up the tree trunk. Dangling from the branc\
h is a rope sliced cleanly at the end. An inflated inner tube sits on the ground. To the North is a campfire surrounded\
 by chairs. To the West is a carport with a couple of cars under it. {southout} {eastout}"
                else:
                    part2 = f"A thick branch juts from a point about 15 feet up the tree trunk. Dangling from the branc\
h is a rope sliced cleanly at the end. To the North is a campfire surrounded by chairs. To the West is a carport with a\
 couple of cars under it. {southout} {eastout}"
                locstrtemp = locdesc[lockey] + part2
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [3, 2]:
                lockey = "".join([str(i) for i in loc])
                locact = locinter[lockey]
                locstuff = []
                locstrtemp = locdesc[lockey]
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [3, 3]:
                locstuff = []
                lockey = "".join([str(i) for i in loc])
                locact = locinter[lockey]
                locstrtemp = locdesc[lockey]
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [11, 2]:
                locact = []
                lockey = "".join([str(i) for i in loc])
                locstuff = locitems[lockey]
                if len(locstuff) == 1:
                    part2 = " and a knife on it. The rest of the barn is divided into pens set up to accommodate animal\
s, but today they are occupied only by sealed crates that smell faintly of alcohol."
                else:
                    part2 = " on it. The rest of the barn is divided into pens set up to accommodate animals, \
but today they are occupied only by sealed crates that smell faintly of alcohol."
                locstrtemp = locdesc[lockey] + part2
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [12, 2]:
                locact = []
                lockey = "".join([str(i) for i in loc])
                locstuff = locitems[lockey]
                if len(locstuff) == 2:
                    part2 = "To your right is a side table. On the table is a plastic key embossed with the Ford logo. \
Hanging from a row of pegs is a coat. Through the window across from you, you can see the range in the distance."
                elif locstuff == ["key"]:
                    part2 = "To your right is a side table. On the table is a plastic key embossed with the Ford logo. \
Through the window across from you, you can see the range in the distance."
                elif locstuff == ["coat"]:
                    part2 = "Hanging from a row of pegs is a coat. Through the window across from you, you can see \
the range in the distance."
                else:
                    part2 = "Through the window across from you, you can see the range in the distance."
                locstrtemp = locdesc[lockey] + part2
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
            case [13, 3]:
                locact = []
                lockey = "".join([str(i) for i in loc])
                locstuff = locitems[lockey]
                if len(locstuff) == 1:
                    part2 = "A Baker Rifle leans against the wall next to one of the openings. The flint is firmly \
seated and the frizzen is rust free. Around you is a sea of trees, slowly undulating in waves of green \
interrupted only by the clearing, the road, and the river. In the distance the trees rise up the side of a rounded \
mountain."
                else:
                    part2 = "Around you is a sea of trees, slowly undulating in waves of green \
interrupted only by the clearing, the road, and the river. In the distance the trees rise up the side of a rounded \
mountain."
                locstrtemp = locdesc[lockey] + part2
                locstr = conlinre(locstrtemp)
                if counter == 0:
                    print(locstr)
                    counter += 1
                    interpret()
                else:
                    interpret()
    if victory == "Y":
        x="\n \n Congratulations, you won! \n \n Written and programmed by Nicolas Proctor \n last updated: 11/24/2023"
        print(conlinre(x))
    elif victory == "Q":
        print("Goodbye")
    elif victory == "X":
        print("---GAME-OVER---")
    else:
        print("gg ez no re")


game()
