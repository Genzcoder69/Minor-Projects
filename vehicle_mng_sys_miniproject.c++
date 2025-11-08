#include<bits/stdc++.h>
using namespace std;

class company
{
    public:
        virtual void showModels()=0;
        virtual void showSpecs(int)=0;
};

class Ferrari : public company
{
    public:
        void showModels()
        {
            cout<<"---Ferrari Available Models---"<<endl;
            cout<<"1>>- Ferrari SF90"<<endl;
            cout<<"2>>- Ferrari Roma"<<endl;
            cout<<"3>>- Ferrari 296 GTB"<<endl;
            cout<<"4>>- Ferrari 812 Competizione"<<endl;
            cout<<"5>>- Ferrari Daytona SP3"<<endl;
        }

        void showSpecs(int choice)
        {
            switch (choice)    
            {
                case 1:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses SF90"<<endl;
                    cout<<"--SF90 Specs--"<<endl;
                    cout<<"* Max Power: 1000HP"<<endl;
                    cout<<"* Top Speed: 340Km/h"<<endl;
                    cout<<"* Engine : V8-3,990cc"<<endl;
                    cout<<"* Price : 3.5Cr"<<endl;
                    break;
                case 2:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses Roma"<<endl;
                    cout<<"--Roma Specs--"<<endl;
                    cout<<"* Max Power: 620HP"<<endl;
                    cout<<"* Top Speed: 320Km/h"<<endl;
                    cout<<"* Engine : V8-3,855cc"<<endl;
                    cout<<"* Price : 2.1Cr"<<endl;
                    break;
                case 3:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses 296 GTB"<<endl;
                    cout<<"--296GTB Specs--"<<endl;
                    cout<<"* Max Power: 830HP"<<endl;
                    cout<<"* Top Speed: 330Km/h"<<endl;
                    cout<<"* Engine : V6-2,560cc"<<endl;
                    cout<<"* Price : 1.3Cr"<<endl;
                    break;
                case 4:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses 812 Competizione"<<endl;
                    cout<<"--812 Competizione Specs--"<<endl;
                    cout<<"* Max Power: 830HP"<<endl;
                    cout<<"* Top Speed: 340Km/h"<<endl;
                    cout<<"* Engine : V12-6,496cc"<<endl;
                    cout<<"* Price : 4.7Cr"<<endl;
                case 5:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses Daytona SP3"<<endl;
                    cout<<"--Daytona SP3 Specs--"<<endl;
                    cout<<"* Max Power: 840HP"<<endl;
                    cout<<"* Top Speed: 340Km/h"<<endl;
                    cout<<"* Engine : V12-6,496cc"<<endl;
                    cout<<"* Price : 5.3Cr"<<endl;
                default:
                    cout<<"Wrong Choice!"<<endl;
                    break;
            }
        }
};

class BMW : public company
{
    public:
        void showModels()
        {
            cout<<"---BMW Available Models---\n";
            cout<<"1>>- BMW M5(G90)"<<endl;
            cout<<"2>>- BMW iX3"<<endl;
            cout<<"3>>- BMW X5(G06)"<<endl;
            cout<<"4>>- BMW X7(SUV)"<<endl;
            cout<<"5>>- BMW Gran coupe"<<endl;
        }

        void showSpecs(int choice)
        {
            switch (choice)    
            {
                case 1:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses M5(G90)"<<endl;
                    cout<<"--M5(G90) Specs--"<<endl;
                    cout<<"* Max Power: 727HP"<<endl;
                    cout<<"* Top Speed: 305Km/h"<<endl;
                    cout<<"* Engine : V8-3,990cc"<<endl;
                    cout<<"* Price : 1.5Cr"<<endl;
                    break;
                case 2:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses iX3"<<endl;
                    cout<<"--iX3 Specs--"<<endl;
                    cout<<"* Max Power: 436HP"<<endl;
                    cout<<"* Top Speed: 320Km/h"<<endl;
                    cout<<"* Engine : EV-Dual Motor"<<endl;
                    cout<<"* Price : 2.6Cr"<<endl;
                    break;
                case 3:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses X5(G06)"<<endl;
                    cout<<"--X5(G06) Specs--"<<endl;
                    cout<<"* Max Power: 379HP"<<endl;
                    cout<<"* Top Speed: 280Km/h"<<endl;
                    cout<<"* Engine : V6-2,260cc"<<endl;
                    cout<<"* Price : 1.37Cr"<<endl;
                    break;
                case 4:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses X7(SUV)"<<endl;
                    cout<<"--X7(SUV) Specs--"<<endl;
                    cout<<"* Max Power: 930HP"<<endl;
                    cout<<"* Top Speed: 330Km/h"<<endl;
                    cout<<"* Engine : V12-3,496cc"<<endl;
                    cout<<"* Price : 3.4Cr"<<endl;
                case 5:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses Gran coupe"<<endl;
                    cout<<"--Gran coupe Specs--"<<endl;
                    cout<<"* Max Power: 640HP"<<endl;
                    cout<<"* Top Speed: 260Km/h"<<endl;
                    cout<<"* Engine : V6-2,135cc"<<endl;
                    cout<<"* Price : 70Lakh"<<endl;
                default:
                    cout<<"Wrong Choice!"<<endl;
                    break;
            }
        }
};

class MercedesBenz : public company
{
    public:
        void showModels()
        {
            cout<<"---Mercedes Available Models---\n";
            cout<<"1>>- AMG A45"<<endl;
            cout<<"2>>- AMG GT55"<<endl;
            cout<<"3>>- AMG GT63"<<endl;
            cout<<"4>>- GLS 600"<<endl;
            cout<<"5>>- GLA 400"<<endl;
        }

        void showSpecs(int choice)
        {
            switch (choice)    
            {
                case 1:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses AMG A45"<<endl;
                    cout<<"--AMG A45 Specs--"<<endl;
                    cout<<"* Max Power: 621HP"<<endl;
                    cout<<"* Top Speed: 290Km/h"<<endl;
                    cout<<"* Engine : V8-2,450cc"<<endl;
                    cout<<"* Price : 1.2Cr"<<endl;
                    break;
                case 2:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses AMG GT55"<<endl;
                    cout<<"--AMG GT55 Specs--"<<endl;
                    cout<<"* Max Power: 496HP"<<endl;
                    cout<<"* Top Speed: 310Km/h"<<endl;
                    cout<<"* Engine : V8-2,360"<<endl;
                    cout<<"* Price : 2.16Cr"<<endl;
                    break;
                case 3:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses AMG GT63"<<endl;
                    cout<<"--AMG GT63 Specs--"<<endl;
                    cout<<"* Max Power: 679HP"<<endl;
                    cout<<"* Top Speed: 320Km/h"<<endl;
                    cout<<"* Engine : V8-3,260cc"<<endl;
                    cout<<"* Price : 3.12Cr"<<endl;
                    break;
                case 4:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses GLS 600"<<endl;
                    cout<<"--GLS 600 Specs--"<<endl;
                    cout<<"* Max Power: 830HP"<<endl;
                    cout<<"* Top Speed: 310Km/h"<<endl;
                    cout<<"* Engine : V12-3,260cc"<<endl;
                    cout<<"* Price : 4.6Cr"<<endl;
                case 5:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses GLA 400"<<endl;
                    cout<<"--GLA 400 Specs--"<<endl;
                    cout<<"* Max Power: 460HP"<<endl;
                    cout<<"* Top Speed: 280Km/h"<<endl;
                    cout<<"* Engine : V8-2,135cc"<<endl;
                    cout<<"* Price : 2.4"<<endl;
                default:
                    cout<<"Wrong Choice!"<<endl;
                    break;
            }
        }
};

class Bugatti : public company
{
    public:
        void showModels()
        {
            cout<<"---Bugatti Available Models---\n";
            cout<<"1>>- Chiron"<<endl;
            cout<<"2>>- Veyron"<<endl;
        }

        void showSpecs(int choice)
        {
            switch (choice)    
            {
                case 1:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses Chiron"<<endl;
                    cout<<"--Chiron Specs--"<<endl;
                    cout<<"* Max Power: 1479HP"<<endl;
                    cout<<"* Top Speed: 420Km/h"<<endl;
                    cout<<"* Engine : W16-5,690cc"<<endl;
                    cout<<"* Price : 28.4Cr"<<endl;
                    break;
                case 2:
                    cout<<"***Congratulations***"<<endl;
                    cout<<"You chooses Veyron"<<endl;
                    cout<<"--Veyron Specs--"<<endl;
                    cout<<"* Max Power: 1001HP"<<endl;
                    cout<<"* Top Speed: 407Km/h"<<endl;
                    cout<<"* Engine : W16-4,860cc"<<endl;
                    cout<<"* Price : 14.6Cr"<<endl;
                    break;
                default:
                    cout<<"Wrong Choice!"<<endl;
                    break;
            }
        }
};


int main()
{
    int model;
    string compChoice;
    company *c = nullptr;

    while(true)
    {
        cout<<"-----Available Cars-----\n";
        cout<<"*Ferrari\n*BMW\n*MercedesBenz\n*Bugatti\n";
        cout<<"-----Enter Car Company-----\n";
        cin>>compChoice;

        if(compChoice == "Ferrari")
        {
            c = new Ferrari;
        }
        else if(compChoice == "BMW")
        {
            c = new BMW;
        }
        else if(compChoice == "MercedesBenz")
        {
            c = new MercedesBenz;
        }
        else if(compChoice == "Bugatti")
        {
            c = new Bugatti;
        }
        else if(compChoice == "Exit")
        {
            cout<<"# # # Thanks # # #\n";
            return 0;
        }
        else
        {
            continue;
        }
        c->showModels();
        cout<<"Enter model : ";
        cin>>model;
        c->showSpecs(model);
        delete c;
    }
}
