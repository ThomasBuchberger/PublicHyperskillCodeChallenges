#include <iostream>
// Created by thoma on 04.06.2025.
//
void displayCamelHabitat() {
    std::string camel = R"(
        Switching on the camera in the camel habitat...
         ___.-''''-.
        /___  @    |
        ',,,,.     |         _.'''''''._
             '     |        /           \\
             |     \\    _.-'             \\
             |      '.-'                  '-.
             |                               ',
             |                                '',
              ',,-,                           ':;
                   ',,| ;,,                 ,' ;;
                      ! ; !'',,,',',,,,'!  ;   ;:
                     : ;  ! !       ! ! ;  ;   :;
                     ; ;   ! !      ! !  ; ;   ;,
                    ; ;    ! !     ! !   ; ;
                    ; ;    ! !    ! !     ; ;
                   ;,,      !,!   !,!     ;,;
                   /_I      L_I   L_I     /_I
        Look at that! Our little camel is sunbathing!)";
    std::cout << camel<<"\n\n\n";
}
void displayLionHabitat() {
    std::string lion = R"(
        Switching on the camera in the lion habitat...
                                                       ,w.
                                                     ,YWMMw  ,M  ,
                                _.---.._   __..---._.'MMMMMw,wMWmW,
                           _.-""        '''           YP"WMMMMMMMMMb,
                        .-' __.'                   .'     MMMMW^WMMMM;
            _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
         ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\\
        ,MM:.    .'.-'   .'     ;     `\\    ;     `,     MMMMMMMW `"=./`-,
        WMMm__,-'.'     /      _.\\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
        "^MP__.-'    ,-' _.--""   `-,   ;       \\  ; ;MMMMMMMMMMW^``; __|
                   /   .'            ; ;         )  )`{  \\ `"^W^`,   \\  :
                  /  .'             /  (       .'  /     Ww._     `.  `"
                 /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
                (--, )                `,_ / `) \\/"")      ^"      `-, -;"\\:
        The lion is roaring!)";
    std::cout <<lion<<"\n\n\n";
};
void displayDeerHabitat() {
    std::string deer = R"(
        Switching on the camera in the deer habitat...
           /|       |\\
        `__\\       //__'
           ||      ||
         \\__`\\     |'__/
           `_\\   //_'
           _.,:---;,._
           \\_:     :_/
             |@. .@|
             |     |
             ,\\.-./ \\
             ;;`-'   `---__________-----.-.
             ;;;                         \\_\\
             ';;;                         |
              ;    |                      ;
               \\   \\     \\        |      /
                \\_, \\    /        \\     |\\
                  |';|  |,,,,,,,,/ \\    \\ \\_
                  |  |  |           \\   /   |
                  \\  \\  |           |  / \\  |
                   | || |           | |   | |
                   | || |           | |   | |
                   | || |           | |   | |
                   |_||_|           |_|   |_|
                  /_//_/           /_/   /_/
        Our 'Bambi' looks hungry. Let's go to feed it!)";
    std::cout << deer<<"\n\n\n";
};
void displayGooseHabitat() {
    std::string goose = R"(
        Switching on the camera in the goose habitat...

                                            _
                                        ,-"" "".
                                      ,'  ____  `.
                                    ,'  ,'    `.  `._
           (`.         _..--.._   ,'  ,'        \\    \\
          (`-.\\    .-""        ""'   /          (  d _b
         (`._  `-"" ,._             (            `-(   \\
         <_  `     (  <`<            \\              `-._\\
          <`-       (__< <           :
           (__        (_<_<          ;
            `------------------------------------------
        The goose is staring intently at you... Maybe it's time to change the channel?)";
    std::cout << goose<<"\n\n\n";
}
void displayBatHabitat() {
    std::string bat = R"(
        Switching on the camera in the bat habitat...
        _________________               _________________
         ~-.              \\  |\\___/|  /              .-~
             ~-.           \\ / o o \\ /           .-~
                >           \\  W  //           <
               /             /~---~\\             \\
              /_            |       |            _\\
                 ~-.        |       |        .-~
                    ;        \\     /        i
                   /___      /\\   /\\      ___\\
                        ~-. /  \\_/  \\ .-~
                           V         V
        This bat looks like it's doing fine.)";

    std::cout << bat<<"\n\n\n";
}
void displayRabbitHabitat() {
    std::string rabbit = R"(
        Switching on the camera in the rabbit habitat...
                 ,
                /|      __
               / |   ,-~ /
              Y :|  //  /
              | jj /( .^
              >-"~"-v"
             /       Y
            jo  o    |
           ( ~T~     j
            >._-' _./
           /   "~"  |
          Y     _,  |
         /| ;-"~ _  l
        / l/ ,-"~    \\
        \\//\\/      .- \\
         Y        /    Y
         l       I     !
         ]\\      _\\    /"\\
        (" ~----( ~   Y.  )
        It looks like we will soon have more rabbits!)";
    std::cout << rabbit<<"\n\n\n";
}
void print_habitat(const int habitat) {
    switch (habitat){
        case 0: displayCamelHabitat(); break;
        case 1: displayLionHabitat(); break;
        case 2: displayDeerHabitat(); break;
        case 3: displayGooseHabitat(); break;
        case 4: displayBatHabitat(); break;
        case 5: displayRabbitHabitat(); break;
        default: std::cout << "This cannot happen" ; break;
    }
}
int main() {
    do{
        std::string userInput;
        std::cout << "Please enter the number of the habitat you would like to view:";
        std::cin >> userInput;

        if (userInput == "exit") {
            std::cout << std::endl << "See you later!" << std::endl;
            return 0;
        }

        int m = std::atoi(userInput.c_str());

        if (m >= 0 && m <= 5) {
            print_habitat(m);
        } else {
            std::cout << std::endl << "Invalid habitat number. Please enter a number between 0 and 5." << std::endl;
        }

    }while(true);



    return 0;
}