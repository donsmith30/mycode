#!/bin/bash

#prompt read input
#make the user from prompt and if group given add to group
#quit prompt function
#while loop to run it all

prompt(){
echo What would you like to name the new user?
read user

echo What group would you like to add the user to, to skip hit enter?
read group 
}

makeUser(){
sudo useradd -p password $user

if [ -z $group ]
then
    echo $user only added to $user group!
else    
    sudo groupadd $group
    sudo  usermod -aG $group $user
    echo $user added to $group!
fi 
}

quit(){
echo would you like to make another user, yes or no?
read make

if [ "${make,,}" != "yes" ]
then
    echo you typed $make, did not indicate yes, exiting program...
    quit="yes"
fi
}

#Start-up
echo ***-WELCOME TO USERADD! V1.0-*** | figlet

#runs the functions until quit option is yes
while [ "$quit" != "yes" ]
do
    prompt
    makeUser
    quit
done
