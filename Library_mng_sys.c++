#include<bits/stdc++.h>
using namespace std;

class details
{
    string id,name,author,search;
    fstream FILE;
    public:
    void addBook();
    void showBook();
    void extractBook();
    void deleteBook();
}obj;

void details::addBook()
{
    cin.ignore();

    cout<<"\nEnter Book Id:";
    getline(cin,id);
    cout<<"Enter Book name:";
    getline(cin,name);
    cout<<"Enter Book's Author name:";
    getline(cin,author);

    FILE.open("bookData.txt",ios::out | ios::app);
    FILE<<id<<"*"<<name<<"*"<<author<<endl;
    FILE.close();
}

void details::showBook()
{
    FILE.open("bookData.txt",ios::in);
    getline(FILE,id,'*');
    getline(FILE,name,'*');
    getline(FILE,author,'\n');
        cout<<"\n\n";
        cout<<"\t\t Book Id \t\t\t Book Name \t\t\t Author's Name"<<endl;
    while(!FILE.eof())
    {
        cout<<"\t\t "<<id<<" \t\t\t "<<name<<" \t\t\t "<<author<<endl;
        getline(FILE,id,'*');
        getline(FILE,name,'*');
        getline(FILE,author,'\n');
    }
    FILE.close();
}

void details::extractBook()
{
    showBook();
    cout<<"Enter Book Id: ";
    getline(cin,search);

    FILE.open("bookData.txt",ios::in);
    getline(FILE,id,'*');
    getline(FILE,name,'*');
    getline(FILE,author,'\n');

    cout<<"\n\n";
    cout<<"\t\t Book Id \t\t\t Book Name \t\t\t Author's Name"<<endl;
    while(!FILE.eof())
    {
        if(search == id)
        {
            cout<<"\t\t "<<id<<" \t\t\t "<<name<<" \t\t\t "<<author<<endl;
            cout<<"<><>Book Extracted successfully<><>";
        }
        getline(FILE,id,'*');
        getline(FILE,name,'*');
        getline(FILE,author,'\n');
    }
    FILE.close();
}

void details::deleteBook()
{
    cin.ignore();
    string del_id;
    cout<<"Enter Book id to delete:";
    getline(cin,del_id);

    fstream FILE,temp;
    FILE.open("bookData.txt",ios::in);
    temp.open("temp.txt",ios::out);

    bool found = false;
    string id,name,author;

    getline(FILE,id,'*');
    getline(FILE,name,'*');
    getline(FILE,author,'\n');

    while(!FILE.eof())
    {
        if(del_id != id)
        {
            temp<<id<<"*"<<name<<"*"<<author<<endl;
        }
        else
        {
            found = true;
        }
        getline(FILE,id,'*');
        getline(FILE,name,'*');
        getline(FILE,author,'\n');
    }
    FILE.close();
    temp.close();
    remove("bookData.txt");
    rename("temp.txt","bookData.txt");

    if(found)
    {
        cout<<"\n<><>Book deleted successfully<><>"<<endl;
    }
    else
    {
        cout<<"\n<><>Book id not found<><>"<<endl;
    }
}


int main()
{
    int choice;

    cout<<"-----------------------"<<endl;
    cout<<"1- Show all books:"<<endl;
    cout<<"2- Extract books:"<<endl;
    cout<<"3- Add books(ADMIN):"<<endl;
    cout<<"4- Delete book:"<<endl;
    cout<<"5- Exit"<<endl;
    cout<<"-----------------------"<<endl;

    cout<<"Enter choice:";
    cin>>choice;
    switch (choice)
    {
    case 1:
        cin.ignore();
        obj.showBook();
        break;
    case 2:
        cin.ignore();
        obj.extractBook();
        break;
    case 3:
        cin.ignore();
        obj.addBook();
        break;
    case 4:
        cin.ignore();
        obj.deleteBook();
        break;
    case 5:
        return 0;
    default:
        cout<<"Invalid character!"<<endl;
    }
}