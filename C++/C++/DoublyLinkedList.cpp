#include "DoublyLinkedList.h"

#include <iostream>

using namespace std;

DoublyLinkedList::DoublyLinkedList ( int data)
{
	// Create the list with the first element with data.
	DoublyLinkedList::Head = DoublyLinkedList::CreateNode ( data );
	cout << "Create a Doubly Linked List with the first node as : ";
	DoublyLinkedList::PrintNode ( Head );
	cout << endl;
}

DoublyLinkedList::DoubleNode* DoublyLinkedList::CreateNode ( int data ){
	DoubleNode* temp = (DoubleNode*)malloc ( sizeof ( DoubleNode ) );
	temp->data = data;
	temp->prevNode = NULL;
	temp->nextNode = NULL;
	return temp;
}

void DoublyLinkedList::PrintNode ( DoubleNode* node ){
	cout << node -> prevNode << "| " << node->data << " |" << node->nextNode;
}

int DoublyLinkedList::GetListLength ( ){
	DoubleNode* node = Head;
	int length = 0;
	while ( node != NULL ){
		length++;
		node = node->nextNode;
	}
	return length;
}

void DoublyLinkedList::Push ( int data ){
	DoubleNode* node = Head;
	while ( node->nextNode != NULL ){
		node = node->nextNode;
	}
	DoubleNode* temp = CreateNode ( data );
	node->nextNode = temp;
	temp->prevNode = node;
}

int DoublyLinkedList::Pop ( ){
	DoubleNode* node = Head;
	while ( node->nextNode != NULL ){
		node = node->nextNode;
	}
	//set the previous node's next node to NULL
	node->prevNode->nextNode = NULL;
	int val = node->data;
	free ( node );
	return val;
}
void DoublyLinkedList::PrintList ( ){
	DoubleNode* curr = Head;
	cout << "START <-- ";
	while ( curr != NULL ){
		PrintNode ( curr );
		cout << " <==> ";
		curr = curr->nextNode;
	}
	cout << " END" << endl;
}

void DoublyLinkedList::Insert ( int pos, int data ){
	DoubleNode* curr = Head;
	DoubleNode* temp = CreateNode ( data );
	if ( pos <= 0 ){
		temp->nextNode = Head;
		Head->prevNode = temp;
		Head = temp;
	}
	else if ( pos >= GetListLength ( ) ){
		Push ( data );
		free ( temp );
	}
	else{
		while ( pos > 0 ){
			curr = curr->nextNode;
			pos--;
		}
		curr->prevNode->nextNode = temp;
		temp->prevNode = curr->prevNode;
		curr->prevNode = temp;
		temp->nextNode = curr;
		
	}

}

int DoublyLinkedList::deleteData ( int data ){
	DoubleNode* curr = Head;
	if ( curr->data == data ){
		curr = curr->nextNode;
		free ( Head );
		Head = curr;
		Head->prevNode = NULL;
		return data;
	}
	else{
		while ( curr->data != data ){
			if ( curr->nextNode == NULL ) return -1;
			curr = curr->nextNode;
		}
		curr->prevNode->nextNode = curr->nextNode;
		if ( curr->nextNode != NULL) curr->nextNode->prevNode = curr->prevNode;
		free ( curr );
		return data;
	}
}
int DoublyLinkedList::Delete ( ){
	cout << "Do you want to delete node with data comparision or position comparision ? (1/2) ... ";
	int choice;
	cin >> choice;
	int ret = -1;
	if ( choice == 1 )
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

int DoublyLinkedList::deletePosition ( int Position ){
	int ret = -1;
	if ( 0 < Position < GetListLength ( ) ){
		DoubleNode* curr = Head;
		if ( Position == 1 ){
			ret = Head->data;
			free ( Head );
			Head = curr->nextNode;
			Head->prevNode = NULL;
		}
		else{
			for ( int i = 1; i < Position - 1; i++ ){
				curr = curr->nextNode;
			}
			DoubleNode* temp = curr->nextNode->nextNode;
			ret = curr->nextNode->data;
			free ( curr->nextNode );
			curr->nextNode = temp;
		}
		return ret;
	}

	return ret;
}


void DoublyLinkedList::deleteList ( ){
	for ( int i = 0; i < GetListLength ( ); i++ ){
		Pop ( );
	}
}
void DoublyLinkedList::Menu ( ){
	while ( 1 ) {
		if ( GetListLength ( ) > 0 ){
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
					cout << "Element that was deleted has a value of : " << Pop ( ) << endl;
					break;
				case 3:
					cout << "Please input the data for the node ... ";
					cin >> data;
					cout << "Please input the position where the node to be inserted ... ";
					cin >> position;
					Insert ( position, data );
					break;
				case 4:
					Delete ( );
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
					return;
			}
		}
		else {
			cout << "There are not more elements left in this list any more." << endl;
			return;
		}
	}
}

DoublyLinkedList::~DoublyLinkedList ( )
{
}
