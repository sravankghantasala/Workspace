#include "SingleLinkedList.h"
#include <iostream>

using namespace std;

SingleLinkedList::SingleLinkedList ( int data){
	// Create the list with the first element with data.
	SingleLinkedList::Head = SingleLinkedList::CreateNode ( data );
	cout << "Create a List with the first node as : ";
	SingleLinkedList::PrintNode ( Head );
	cout << endl;
}

SingleLinkedList::SingleNode* SingleLinkedList::CreateNode ( int data ){
	SingleNode* temp = (SingleNode*)malloc ( sizeof ( SingleNode ) );
	temp->data = data;
	temp->nextNode = NULL;
	return temp;
}

void SingleLinkedList::PrintNode ( SingleLinkedList::SingleNode* Node ){
	cout << "| " << Node->data << " | ";
}

void SingleLinkedList::PrintList ( ){
	if ( GetListLength() > 0 ) {
		SingleNode* node = Head;
		while ( node != NULL ){
			PrintNode ( node );
			cout << " --> ";
			node = node->nextNode;
		}
		cout << endl;
	}
	else{
		cout << "There are no Elements in the list" << endl;
	}
}

void SingleLinkedList::Insert ( int data, int pos ){
	SingleNode* temp;
	if ( pos == 0 ){
		//Create the First element and update Head
		temp = Head->nextNode;
		free ( Head );
		Head = temp;
	}
	else if ( pos >= GetListLength ( ) ){
		Push ( data );
	}
	else{
		SingleNode* curr = Head;
		for ( int i = 1; i < pos-1; i++ ){
			curr = curr->nextNode;
		}
		SingleNode* temp = CreateNode ( data );
		temp->nextNode = curr->nextNode;
		curr->nextNode = temp;
	}
}

int SingleLinkedList::Delete ( ){
	cout << "Do you want to delete node with data comparision or position comparision ? (1/2) ... ";
	int choice;
	cin >> choice;
	int ret = -1;
	if (choice == 1)
	{ 
		cout << "Enter the data value you want to delete node";
		int data;
		cin >> data;
		ret = deleteData ( data ); 
		if ( ret != -1 ) cout << "Node deleted successfully!" << endl;
		else cout << "A node with the given value is not in the list!" << endl;
		cout << "List after deleting a node ... " << endl;
		PrintList ( );
	}
	else if ( choice == 2 ) { 
		cout << "Enter the position in the list you want to delete node [min: 1, max :" << GetListLength ( ) << "] ... ";
		int pos;
		cin >> pos;
		ret = deletePosition ( pos ); 
		if ( ret != -1 ) cout << "Node deleted successfully!" << endl;
		else cout << "Position is out of bounds!" << endl;
		cout << "List after deleting a node ... " << endl;
		PrintList ( );
	}
	else {
		cout << "You can't delete a node using both data and position at a time ! huh!" << endl;
	}
	
	return ret;
}

int SingleLinkedList::deleteData ( int data ){
	SingleNode* curr = Head;
	if ( curr->data == data ){
		curr = curr->nextNode;
		free ( Head );
		Head = curr;
		return data;
	}
	else{
		while ( curr->nextNode->data != data ){
			if ( curr->nextNode == NULL ) return -1;
			curr = curr->nextNode;
		}
		SingleNode* temp = curr->nextNode->nextNode;
		free ( curr->nextNode );
		curr->nextNode = temp;
		return data;
	}
}

int SingleLinkedList::deletePosition ( int Position ){
	int ret = -1;
	if ( 0 < Position < GetListLength ( ) ){
		SingleNode* curr = Head;
		if ( Position == 1 ){
			SingleNode* temp = curr->nextNode;
			ret = Head->data;
			free ( Head );
			Head = temp;
		}
		else{
			for ( int i = 1; i < Position - 1; i++ ){
				curr = curr->nextNode;
			}
			SingleNode* temp = curr->nextNode->nextNode;
			ret = curr->nextNode->data;
			free ( curr->nextNode );
			curr->nextNode = temp;
			}
		return ret;
	}

	return ret;
}

void SingleLinkedList::deleteList ( ){
	while( GetListLength ( ) > 0 ){
		Pop ( );
	}
}

void SingleLinkedList::Push ( int data ){
	SingleNode* node = Head;
	while ( node->nextNode != NULL ){
		node = node->nextNode;
	}
	SingleNode* temp = CreateNode ( data );
	node->nextNode = temp;
}

int SingleLinkedList::GetListLength ( ){
	SingleNode* node = Head;
	int length = 0;
	while ( node != NULL ){
		length++;
		node = node->nextNode;
	}
	return length;
}

int SingleLinkedList::Pop ( ){
	SingleNode* curr = Head;
	int value = -1;
	if ( GetListLength ( ) > 1 ){
		while ( curr->nextNode->nextNode != NULL ){
			curr = curr->nextNode;
		}
		value = curr->nextNode->data;
		curr->nextNode = NULL;
		free ( curr->nextNode );
	}
	else{
		cout << "Deleting the last Node of the List ... " << endl;
		Head = NULL;
		value = curr->data;
	}
	
	
	cout << "The element deleted has this value : " << value <<endl;
	
	return value;
}

void SingleLinkedList::Menu ( ){
	while ( 1 ) {
		if ( GetListLength() > 0 ){
			cout << "Actions Possible with this data structure are ... " << endl
				<< "\t1. Append Node" << endl
				<< "\t2. Delete Last Node" << endl
				<< "\t3. Insert Node at position" << endl
				<< "\t4. Delete Node" << endl
				<< "\t5. Know Size of the List" << endl
				<< "\t6. Print List" << endl
				<< "\t7. Delete List" << endl
				<< "\t8. Exit " << endl << endl
				<< "Please choose what you want to do with this list ... ";

			int choice;
			cin >> choice;

			int data, position;
			switch ( choice ) {
				case 1:
					cout << "Please input the data for the node ... ";
					cin >> data;
					Push ( data );
					break;
				case 2:
					Pop ( );
					break;
				case 3:
					cout << "Please input the data for the node ... ";
					cin >> data;
					cout << "Please input the position where the node to be inserted ... ";
					cin >> position;
					Insert ( data, position );
					break;
				case 4:
					Delete( );
					break;
				case 5:
					cout << "Length of the list is : " << GetListLength ( ) << endl;
					break;
				case 6:
					PrintList ( );
					break;
				case 7:
					deleteList ( );
					break;
				case 8:
					deleteList ( );
					return;
			}
		}
		else {
			cout << "There are not more elements left in this list any more." << endl;
			return;
		}
	}
}

SingleLinkedList::~SingleLinkedList ( )
{
}
