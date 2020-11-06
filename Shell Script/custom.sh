#!/bin/bash

#EXTRACTING FILES EHEHEHE

function compile()
{
    FILE=$1
    if [ -z "$FILE" ];then
        echo -e "You haven't specified the file yet"
        echo -e "Please specify the file!"
    elif [ "${FILE: -4}" == '.cpp' ];then
        g++ "$FILE" -o hehe
        if [ $? -eq 0 ];then
            echo -e "Compile Succedded"
            echo -e "Output: hehe"
            echo -e "Please run it by using ./hehe"
        else
            echo -e "Compile Failed"
            echo -e "Check above if there are any error"
        fi
    elif [ "${FILE: -2}" == '.c' ];then
        gcc "$FILE" -o hehe
        if [ $? -eq 0 ];then
            echo -e "Compile Succedded"
            echo -e "Output: hehe"
            echo -e "Please run it by using ./hehe"
        else
            echo -e "Compile Failed"
            echo -e "Check above if there are any error"
        fi
    elif [ "${FILE: -5}" == '.java' ];then
        javac "$FILE"
        if [ $? -eq 0 ];then
            echo -e "Compile Succedded"
            echo -e "Please check the file below"
            echo -e "Run the file with .class with java"
            ls
        else
            echo -e "Compile Failed"
            echo -e "Check above if there are any error"
        fi
    fi
}

function_rar()
{
    echo -e "Aightt im going to extract this rar file : $1"
    echo -e "If you think you're making a mistake"
    echo -e "Please use CTRL-C"
    sleep 5
    echo -e "Olraitt no cancelation i supposed, starting now...\n"
    echo -e "#####################################################"
    unrar x "$1" && rm "$1"
    echo -e "#####################################################"
    echo -e "Extraction completed!"
    return 1
}

function_zip()
{
        echo -e "Aightt im going to extract this zip file : $1"
        echo -e "If you think you're making a mistake"
        echo -e "Please use CTRL-C"
        sleep 5
        echo -e "Olraitt no cancelation i supposed, starting now...\n"
        echo -e "#####################################################"
        unzip "$1" && rm "$1"
        echo -e "#####################################################"
        echo -e "Extraction completed!"
        return 1
}
function_tar()
{
        echo -e "Aightt im going to extract this tar file : $1"
        echo -e "If you think you're making a mistake"
        echo -e "Please use CTRL-C"
        sleep 5
        echo -e "Olraitt no cancelation i supposed, starting now...\n"
        echo -e "#####################################################"
        tar -xzvf "$1" && rm "$1"
        echo -e "#####################################################"
        echo -e "Extraction completed!"
        return 1
}
function extract()
{
        #DETERMINE THE FILE PATH
        FILE=$1

        #THEN CHECK THE EXISTING PATH
        if [ -z "$FILE" ]; then
                echo -e "\n#####################################################"
                echo -e "You haven't specified the path yet"
                echo -e "Type [extract -h] to get information about this"
                echo -e "#####################################################\n"
        elif [ "$FILE" == "-h" ]; then
                echo -e "\n#####################################################"
                echo -e "This is my own custom script to extract things!"
                echo -e "You can use this command by using extract [path_to_the_file]"
                echo -e "It can determine by itself, whether its .rar .zip .tar .tar.gz .tar.xz"
                echo -e "It will extract the file for you! In the same directory~"
                echo -e "#####################################################\n"
        else
                if [ "${FILE: -4}" == '.rar' ]; then
                        function_rar "$FILE"
                elif [ "${FILE: -4}" == '.zip' ]; then
                        function_zip "$FILE"
                elif [ "${FILE: -4}" == '.tar' ] || [ "${FILE: -7}" == '.tar.gz' ] || [ "${FILE: -7}" == '.tar.xz' ]; then
                        function_tar "$FILE"
                else
                        echo -e "Sorry i guess the file you're trying to extract can't be processed atm"
                fi
        fi
}
