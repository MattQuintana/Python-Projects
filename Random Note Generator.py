__author__ = 'Matt Q'
import random
#print (random.randrange(1,13))
noteNum = input("How many notes do you want? ")
noteNum = int(noteNum)
#x = random.randrange(1,13)
#otave = random.randrange(1,6)

#print(x)
full_notes = {1: "A",
              2: "A#/Bb",
              3: "B",
              4: "C",
              5: "C#/Db",
              6: "D",
              7: "D#/Eb",
              8: "E",
              9: "F",
              10: "F#/Gb",
              11: "G",
              12: "G#/Ab"}



ckey = [4, 6, 8, 9, 11, 1, 3, 4]
gkey = [11, 1, 3, 4, 6, 8, 10, 11]
dkey = [6, 8, 10, 11, 1, 3, 5, 6]
akey = [1, 3, 5, 6, 8, 10, 12, 1]
ekey = [8, 10, 12, 1, 3, 5, 7, 8]
bkey = [3, 5, 7, 8, 10, 12, 2, 3]
fskey = [10, 12, 2, 3, 5, 7, 9, 10]

fkey = [9, 11, 1, 2, 4, 6, 8, 9]
bfkey = [2, 4, 6, 7, 9, 11, 1, 2]
efkey = [7, 9, 11, 12, 2, 4, 6, 7]
afkey = [12, 2, 4, 5, 7, 9, 11, 12]
dfkey = [5, 7, 9, 10, 12, 2, 4, 5]
gfkey = [10, 12, 2, 3, 5, 7, 9, 10]

chord_keys = {"c": ckey,
              "g": gkey,
              "d": dkey,
              "a": akey,
              "e": ekey,
              "b": bkey,
              "f#": fskey,
              "f": fkey,
              "bb": bfkey,
              "eb": efkey,
              "ab": afkey,
              "db": dfkey,
              "gb": gfkey,
              "a#": bfkey,
              "d#": efkey,
              "c#": dfkey,
              "g#": afkey}
key = chord_keys[input("What key do you want this in? ").lower()]

#key = efkey
#print(key)


for i in key:
    someNote = full_notes[i]
    print(someNote, end = " ")
    #print(someNote, end = " ")

print()
print()

for noteNum in range(0,noteNum):
    x = random.randrange(1,13)
    otave = random.randrange(3,6)
    note_length = random.randint(0,5)
    #print(note_length)
    lengths = [0,1,2,4,8,16]
    note_length = lengths[note_length]
    if x in key:
        print(full_notes[x],otave,note_length)
    else:
        if x == 12:
            print(full_notes[x-1], otave, note_length)
        else:
            print(full_notes[x+1], otave, note_length)

def make_minor():
    #print(key[3])
    #print(key[7])
    minor_note1 = key[3]-1
    minor_note2 = key[7]-1
    #print(minor_note1)
    #print(minor_note2)
make_minor()

print()

major_key = [0,2,2,1,2,2,2,1]
minor_key = [0,2,1,2,2,2,1,2]
minor_pentatonic = [0, 3, 2, 2, 3, 2]
ahava_raba = [0, 1, 3, 1, 2, 1, 2, 2]
natural_minor = [0, 2, 1, 2, 2, 1, 2, 2]
super_locrian = [0, 1, 2, 1, 2, 2, 2, 2]


def new_scales():
    #new_number = random.randrange(1,12)
    new_number = key[0];
    #print(new_number)
    current_scale = []

    semitone_distance = new_number
    for scale_key in minor_key:
        semitone_distance += scale_key
        if semitone_distance == 13:
            semitone_distance = 1
            current_scale.append(full_notes[semitone_distance])
            #print(full_notes[semitone_distance], end = " ")
        elif semitone_distance == 14:
            semitone_distance = 2
            current_scale.append(full_notes[semitone_distance])
            #print(full_notes[semitone_distance], end = " ")
        elif semitone_distance == 15:
            semitone_distance = 3
            current_scale.append(full_notes[semitone_distance])
            #print(full_notes[semitone_distance], end = " ")
        else:
            #print(full_notes[semitone_distance], end = " ")
            current_scale.append(full_notes[semitone_distance])

    for note in current_scale:
            print(note, end = " ")

    print()
    #print(current_scale)

new_scales()

def make_random_notes():
    ### Gets the input for number of notes to produce and turns the input into an integer
    amountOfNotes = input("How many notes do you want? ")
    amountOfNotes = int(amountOfNotes)

    for noteNum in range(0,amountOfNotes):
        x = random.randrange(1,13)
        otave = random.randrange(3,6)
        if x in key:
            print(full_notes[x],otave)
        else:
            if x == 12:
                print(full_notes[x-1], otave)
            else:
                print(full_notes[x+1], otave)

