#! /bin/bash

#THIS IS NOTIFICATION 
#THINGY
#I JUST WANNA #TEST IT OUT

QUOTES=(
    "Semangat yahhh!!"
    "Yuk bisa yuk!!"
    "Jangan gampang menyerah ehehehe"
    "Hayuuu bisa kamu mah"
)

len=${#QUOTES[@]}
countRand=$(($RANDOM%20))

#Trying to make it fully random
#So it will look like this
for i in $(seq 0 $countRand)
do
    R=$(($RANDOM%$len))
done


while true
do
    notify-send 'Halo!!' "${QUOTES[R]}" -i face-smile
    sleep 600
done