#include <iostream>
using namespace std;
int main(){
    /*

    QUESTION 2
Write a program that prompts the user to enter five test scores and then prints the
average test score. (Assume that the test scores are decimal numbers.)

    */

    float score_0 ,score_1 , score_2, score_3, score_4 ;
   
   if(int i=0 ; i<5 ; i++){
    cout "Type in the next test score : " ;
    cin >> score_i;
        while(i == 5){
            cout << "the first test score is " << score_0 << endl ;
            cout << "the second test score is " << score_1 << endl ;
            cout << "the third test score is " << score_2 << endl ;
            cout << "the fourth test score is " << score_3 << endl ;
            cout << "the fifth test score is " << score_4 << endl ;
            float sum = score_0 + score_1 + score_2 + score_3 + score_4 ;
            cout << "The sum of the five test scores is " << sum << endl;
            const float num = 5 ;
            float average = (sum) / num ;
            cout <, "The average of the five numbers is " << average << endl ;


        }
   }
    return 0;
}