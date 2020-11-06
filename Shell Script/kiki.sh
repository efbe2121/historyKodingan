#!/bin/bash

# Author 
# Yow
#
# Just ask me if you need anything

QUOTES=(
    "I have always believed that each man makes his own happiness and is responsible for his own problems. It is a simple philosophy"
    "When we have respect for ourselves and others, we gravitate towards connections that encourage that"
    "Anger is the   ultimate destroyer of your own peace of mind"
    "A man should have the aim and the determination to be honest and upright and sincere in all that he undertakes. If he adds persistency to this he can hardly help being successful"
    "Only one thing is ever guaranteed, that is that you will definitely not achieve the goal if you don't take the shot"
    "Don't be afraid. Be focused. Be determined. Be hopeful. Be empowered"
    "The fact is that grief today is a family matter as much a s it is an individual one"
    "No one would have crossed the ocean if he could have gotten off the ship in the storm"
    "Congratulations! today is your day. You're off to Great Places! You're off and away"
    "Appreciate those early influences and what they've done for you"
    "Emotional empathy is what motivates us to help others"
    "The true wealth of a nation lies not in it's gold or silver but in it's learning, wisdom and in the uprightness of its sons"
    "Make the decision, make another. Remake one past, you cannot"
)

len=${#QUOTES[@]}
countRand=$(($RANDOM%20))

function givequote()
{
    #Trying to make it fully random
    #So it will look like this
    for i in $(seq 0 $countRand)
    do
        R=$(($RANDOM%$len))
    done
    
    echo -e "######################################"
    echo -e "Here's a quote to start your day: "
    echo -e ${QUOTES[$R]}
    echo -e "\nHave a good day!!"
    echo -e "######################################"
}