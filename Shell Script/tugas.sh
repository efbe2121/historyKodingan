function_box()
{
  zenity --info --title "Hai kamu yang jauh disana" --text "Kangen sih pen peluk tapi ya apa daya" --width=300 --height=200
  zenity --question --text "Masih marah kah sama ku?" --ok-label "Nyebelin banget" --cancel-label="Ngga kok" --width=300 --height=200

  if [ $? -eq 0 ];then
    zenity --info --title "Yah masih marah" --text "Maafin aku yah karena lupa :(" --width=300 --height=200
    sleep 2s
    notify-send "Aduh aku ngapain sih" "Aku gabisa pake kata-kata bisanya peluk doang" -i face-smile
    zenity --question --text "Serius marah kah??" --ok-label "Boong tadi" --cancel-label="Iya" --width=300 --height=200
    if [ $? -eq 0 ]; then
      zenity --info --title "Yeeey maaf yah" --text "Kamu tu seseorang yang the best banget, dan juga ga ada yang bisa gantiin kamu, jadi maafin aku banget yahhhh cius" --width=300 --height=200
      sleep 2s
      notify-send "AHHH SENENG" "Lapyu ehe" -i love
      sleep 1s
      xdg-open https://media.tenor.com/images/c5caf59fd029c206db34cbb14956b8e2/tenor.gif
    else
      zenity --info --title "Ahh okay um im sorry" --text "Kamu tu seseorang yang the best banget, dan juga ga ada yang bisa gantiin kamu, jadi maafin aku banget yahhhh cius" --width=300 --height=200
      sleep 2s
      notify-send "Ini notif" "Maaf yah qq <3" -i love
      zenity --question --text "Dimaafin ga aku??" --ok-label "Iya" --cancel-label="Gamau" --width=300 --height=200
      if [ $? -eq 0 ]; then
        zenity --info --title "Yeeey maaf yah" --text "Kamu tu seseorang yang the best banget, dan juga ga ada yang bisa gantiin kamu, jadi maafin aku banget yahhhh cius" --width=300 --height=200
        sleep 2s
        notify-send "AHHH SENENG" "Lapyu ehe" -i love
        xdg-open https://media.tenor.com/images/c5caf59fd029c206db34cbb14956b8e2/tenor.gif
      else
        zenity --info --title "Aku mau nanya deh" --text "Biar komunikasi kita lancar yah, aku mo buka link bentarr, nanti kamu isi yaah" --width=300 --height=200
        sleep 2s
        xdg-open https://docs.google.com/forms/d/1fY06A8nySFdTsZmivPgNiZP24uomc6BhPb3mg9FdElI
        sleep 2s
        notify-send "Jawab yang jujur yah" "Lapyu ehe" -i love
      fi
    fi
  else
    zenity --question --text "Serius??" --ok-label "Iya" --cancel-label="Boong tadi" --width=300 --height=200
    if [ $? -eq 0 ]; then
      zenity --info --title "Yeeey maaf yah" --text "Kamu tu seseorang yang the best banget, dan juga ga ada yang bisa gantiin kamu, jadi maafin aku banget yahhhh cius" --width=300 --height=200
      sleep 2s
      notify-send "AHHH SENENG" "Lapyu ehe" -i love
      xdg-open https://media.tenor.com/images/c5caf59fd029c206db34cbb14956b8e2/tenor.gif
    else
      zenity --info --title "Ahh okay um im sorry" --text "Kamu tu seseorang yang the best banget, dan juga ga ada yang bisa gantiin kamu, jadi maafin aku banget yahhhh cius" --width=300 --height=200
      sleep 2s
      notify-send "Ini notif" "Maaf yah qq <3" -i love
      zenity --question --text "Dimaafin ga aku??" --ok-label "Iya" --cancel-label="Gamau" --width=300 --height=200
      if [ $? -eq 0 ]; then
        zenity --info --title "Yeeey maaf yah" --text "Kamu tu seseorang yang the best banget, dan juga ga ada yang bisa gantiin kamu, jadi maafin aku banget yahhhh cius" --width=300 --height=200
        sleep 2s
        notify-send "AHHH SENENG" "Lapyu ehe" -i love
        xdg-open https://media.tenor.com/images/c5caf59fd029c206db34cbb14956b8e2/tenor.gif
      else
        zenity --info --title "Aku mau nanya deh" --text "Biar komunikasi kita lancar yah, aku mo buka link bentarr, nanti kamu isi yaah" --width=300 --height=200
        sleep 2s
        xdg-open https://docs.google.com/forms/d/1fY06A8nySFdTsZmivPgNiZP24uomc6BhPb3mg9FdElI
        sleep 2s
        notify-send "Jawab yang jujur yah" "Lapyu ehe" -i love
      fi
    fi
  fi
}

zenity -h &> /dev/null
if [ $? -eq 0 ];then
  function_box
else
  sudo apt-get install zenity -y
  function_box
fi
