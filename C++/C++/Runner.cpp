//This program actually calls all the data structures

#include "SingleLinkedList.h"
#include "DoublyLinkedList.h"

#include <iostream>

using namespace std;

void Menu ( ){
	while ( 1 ){
		cout << "Available Datastructures ... " << endl;
		cout << "\t1. Single Linked List" << endl
			 << "\t2. Doubly Linked List" << endl
			 << "\t0. Exit" << endl
			 << endl;
		cout << "Please choose the data structure you want to play with ... ";
		int choice;
		cin >> choice;
		int value;
		switch ( choice ){
			case 0:
				return;
			case 1:
				{
					cout << "Please enter an Integer value to start creating Singly Linked List ... ";
					cin >> value;
					SingleLinkedList SLL ( value );
					SLL.Menu ( );
					break;
				}
			case 2:
				{
					cout << "Please enter an Integer value to start creating Doubly Linked List ... ";
					cin >> value;
					DoublyLinkedList DLL ( value );
					DLL.Menu ( );
					break;
				}
			
		}
	}
}

int main ( ){
	Menu ( );
	
	int ex;
	cin >> ex;
	return 0;
}