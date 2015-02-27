#ifndef DOUBLYLINKEDLIST_H_
#define DOUBLYLINKEDLIST_H_
class DoublyLinkedList
{
public:
	DoublyLinkedList ( int );
	~DoublyLinkedList ( );

	typedef struct DoubleNode{
		int data;
		DoubleNode* prevNode;
		DoubleNode* nextNode;
	};

	DoubleNode* Head;

	DoubleNode* CreateNode ( int );
	void Insert ( int, int );
	void Push ( int );
	int Pop ( );
	int Delete ( );
	int deletePosition ( int );
	int deleteData ( int );
	void deleteList ( );
	void PrintNode ( DoubleNode* );
	void PrintList ( );
	int GetListLength ( );
	void Menu ( );
};

#endif DOUBLYLINKEDLIST_H_

