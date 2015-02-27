class SingleLinkedList
{
public:
	SingleLinkedList ( int );
	~SingleLinkedList ( );

	typedef struct SingleNode{
		int data;
		SingleNode* nextNode;
	};

	SingleNode* Head;
	
	SingleNode* CreateNode ( int  );
	void Insert ( int , int  );
	void Push ( int );
	int Pop ( );
	int Delete ( );
	int deletePosition ( int );
	int deleteData ( int );
	void deleteList ( );
	void PrintNode ( SingleNode* );
	void PrintList ( );
	int GetListLength ( );
	void Menu ( );
};

