#include <iostream>
#include <random>
#include <string>
#include <sstream>
using namespace std;
int rps_game(std::string,std::string,int);

int main() {
    std::cout << "Welcome to Rock, Paper, Scissors Game!\n\n";
    std::cout << "Please enter your name, number of repetitions,\nand your chosen steps\n";
    std::cout << "1 - Rock,\n2 - Paper,\n3 - Scissors:\n";
    std::string input_string,name,word;
    int repnum, count=1, score,score_player, score_computer;
    do{
        score,score_player = 0;
        score_computer = 0;
        std::getline(std::cin, input_string);
        istringstream iss(input_string);
        std:cout<<"InputString: "<<input_string;
        iss >> name;
        iss >> repnum;
        std::cout << "\nGame Start!\n";
        while(iss>>word){
            if (count>repnum)
                break;

            while (true){
                score = rps_game(word,name,count);
                if (score == 1){
                    score_player += 1;
                    break;
                }
                if(score == -1){
                    score_computer += 1;
                    break;
                }
            }
            count++;
        }
        std::cout << "\n\nGame Over!\n";
        std::cout << "Total Score - " <<name<<": " << score_player<<", Computer: "<< score_computer << "\n";
        std:: cout << "Would you like to play again? (yes/no)";
        std::cin >> input_string;
    }while(input_string=="yes");
}
int rps_game(std::string move,std::string name,int round){

    std:std::vector<std::string> moves={"Rock","Paper","Scissors"};
    std::random_device rd;   // Seed with a real random value, if available
    std::mt19937 gen(rd());  // Standard mersenne_twister_engine seeded with rd()
    // Generate and print a random number between 0 and 9
    int random_choice = gen() % 3,mychoice_index = 0,i,returnscore=0;

    std::string computer_move, move_low;


    if(move == "1"||move == "2"||move == "3") {
        move_low = moves[stoi(move)-1];
    }
    else{
        i = 0;
        for (char c : move) {
            if (i==0){
                move_low += toupper(c);
            }
            else{
                move_low += tolower(c);
            }
            i++;
        }
    }
    if(move_low != "Rock" && move_low != "Paper" && move_low !="Scissors") {
        std::cout << "> " << move<<"\n";
        std::cout  << "Invalid move. Please enter Rock, Paper, or Scissors.\n";

    }
    else {
        //std::cout  << "> "   << move<<"\n";

        for(int j = 0; j < moves.size(); j++) {
            if (moves[j] == move_low) {
                mychoice_index = j;
                break;
            }
        }

        if (random_choice == mychoice_index) {
            //std::cout << "It's a draw.\n";
            returnscore = 0;
        }
        else{
            std::cout << "Round " << round << ": ";
            std::cout << "Computer chose " << moves[random_choice]<<", ";
            std::cout << name <<" chose " << move_low<<". ";
            if (random_choice == 0 && mychoice_index == 1) {
                std::cout << "Winner: " << name <<"\n";
                returnscore = 1;
            }
            else if (random_choice == 0 && mychoice_index == 2) {
                std::cout << "Winner: Computer\n";
                returnscore = -1;
            }
            else if (random_choice == 1 && mychoice_index == 0) {
                std::cout << "Winner: Computer\n";
                returnscore = -1;
            }
            else if (random_choice == 1 && mychoice_index == 2) {
                std::cout << "Winner: " << name <<"\n";
                returnscore = 1;
            }
            else if (random_choice == 2 && mychoice_index == 0) {
                std::cout << "Winner: " << name <<"\n";
                returnscore = 1;
            }
            else if (random_choice == 2 && mychoice_index == 1) {
                std::cout << "Winner: Computer\n";
                returnscore = -1;
            }
        }
        return returnscore;
    }
}

//
// Created by thoma on 05.06.2025.
//
