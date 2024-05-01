#include <fstream>
#include <iostream>
#include <limits>
#include <string>
using namespace std;


// Function declarations
void appendEntry();
void createEntry();
void readEntry();
string getFileName();


/**
 * The main function will loop through the file management system
*/
int main()
{
    cout << "Welcome to the File Management System!" << endl;

    // While loop for operations, run until exit or End-Of-File (EOF)
    while (true)
    {
        cout << endl;
        cout << "Choose an operation:" << endl;
        cout << "(x) : Exit" << endl;
        cout << "(n) : Creat a New File" << endl;
        cout << "(r) : Read a File" << endl;
        cout << "(a) : Append to an existing file" << endl;

        char choice;
        cin >> choice;

        // Check if the user wants to exit
        if (!cin || choice == 'x')
        {
            // Return from program
            break;
        }

        // Reset the state of the cin stream
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        switch (choice)
        {
        case 'n':
            createEntry();
            break;
        case 'r':
            readEntry();
            break;
        case 'a':
            appendEntry();
            break;
        default:
            cout << "ERROR: Invalid input. Choose again." << endl;
            break;
        }
    }

    return 0;   // Return 0 on success
}


/**
 * This function will append text to an existing file entry
*/
void appendEntry()
{
    string name = getFileName();
    string filename = name + ".txt";

    ofstream fileManagementSystem;
    fileManagementSystem.open(filename, ofstream::app); // Open the file for appending new texts

    cout << "Type your file name for " << name << " (Enter END on a new line when done.):" << endl;

    string line;
    while (getline(cin, line))
    {
        if (line == "END")
        {
            break;
        }
        fileManagementSystem << line << endl;
    }

    fileManagementSystem.close();
}


/**
 * This function will create a new file entry
*/
void createEntry()
{
    string name = getFileName();
    string filename = name + ".txt";

    cout << "Type your file name for " << name << " (Enter END on a new line when done.):" << endl;

    ofstream fileManagementSystem(filename);

    string line;
    while (getline(cin, line))
    {
        if (line == "END")
        {
            break;
        }
        fileManagementSystem << line << endl;
    }

    fileManagementSystem.close();
}


/**
 * This function will read an entry file and print that file to the terminal
*/
void readEntry()
{
    string name = getFileName();
    string filename = name + ".txt";

    // TODO: Write your code here.
    ifstream fileManagementSystem;
    fileManagementSystem.open(filename); // open the file

    if (!fileManagementSystem)
    {
        cout << "Could not find file entry for " << name << endl;
        return;
    }

    string line;
    while (getline(fileManagementSystem, line))
    {
        cout << line << endl;
    }

    fileManagementSystem.close();
}


string getFileName()
{
    string name;
    cout << "Please enter the file name without white spaces: ";
    cin >> name;

    // Return the date
    return name;
}
