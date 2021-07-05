#MAD LIBS game

Story1part1 = 'Lets start the story: _______ (complete with a noun) '


a = 0

Stories = ['a', ]

NumofStories = Stories.count('a')

Story1 = "It was a ________ (adjetive), cold november day"

print 'Hi, Welcome to the Mad libs Game created by Alex; In this game you will create a story based on any words you wish (They can be invented words)'
print "Now select a number from 1 to:"
print NumofStories

SelectedStory = input()
    
if SelectedStory == 1:
    print Story1part1
    Part1que1 = raw_input()
    print 'The word selected was:'
    print Part1que1
    print  ' %s is having a _______ (complete with a theme) party' % ( Part1que1 ,)
    
    Part1que2 = raw_input()
    print 'The new word selected was:'
    print Part1que2
    print ' %s is having a %s party.Its going to be at ______ (choose a place)' % ( Part1que1 , Part1que2 ,)

    print 'Ohh great choice,lets continue thats our story'
    Part1que3 = raw_input()
    print '%s is having a %s party. Its going to be at %s on ________ (day of the week)' % ( Part1que1 , Part1que2 ,Part1que3 )
    
    print 'When the party is going to take place?'
    Part1que4 = raw_input()
    print '%s is having a %s party. Its going to be at %s on %s (day of the week)' % ( Part1que1 , Part1que2 ,Part1que3 ,Part1que4)
    