/*
This is one of the simplest projects to start with to learn about file systems in C++.
The project involves a user registration process by asking username and password.
Upon successful registration,
a user file is created with the credentials.
If the user does not exist, upon login,
an error will be shown.
You will also learn how to use Visual Studio to create a simple project.
*/
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
    while(true){ //menu loop
    cout << "1) login\n";
    cout << "2) sign-up\n";
    cout << "3) exit\n";
    cout << "pick a option: ";
    int option;
    cin >> option;
    cout << "you have picked option: " << option << endl;
    if(option==1){ // user is attempting to login
    while(true){
        string username;
        string password;
        cout << "enter your username: ";
        cin >> username;
        cout << "enter your password: ";
        cin >> password;        
        
        break;
    } 
    }else if(option==2){ // user is attempting to create a account
    while(true){
        string create_username;
        string create_password;
        cout << "create username: ";
        cin >> create_username;
        cout << "create password; ";
        cin >> create_password;
        ofstream MyFile;
        MyFile.open("reg.txt", ofstream::app);
        MyFile << create_username << ", "<< create_password << endl;
        MyFile.close();
        cout << "username: " << create_username << "password: " << create_password << "created\n";
        cout << "please continue back to the menu\n";
        
        break;
    }
    
    }else if(option==3){ // user is quiting
    break;    
    }
    }

}