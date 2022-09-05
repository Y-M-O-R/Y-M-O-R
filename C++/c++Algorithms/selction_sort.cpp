#include<iostream>  / not made by me
using namespace std;  
int findSmallest (char[],int);  
int main ()  
{  
    char myarray[10] = {'a','v','c','d','e','j','g','x','y'};  
    int pos,temp,pass=0;  
    cout<<"\n Input list of elements to be Sorted\n";  
    for(int i=0;i<10;i++)  
    {  
        cout<<myarray[i]<<"\t";  
    } 
    for(int i=0;i<10;i++)  
    {  
        pos = findSmallest (myarray,i);  
        temp = myarray[i];  
        myarray[i]=myarray[pos];  
        myarray[pos] = temp; 
        pass++;
    }  
    cout<<"\n Sorted list of elements is\n";  
    for(int i=0;i<10;i++)  
    {  
        cout<<myarray[i]<<"\t";  
    } 
    cout<<"\nNumber of passes required to sort the array: "<<pass;
    return 0;  
}  
int findSmallest(char myarray[],int i)  
{  
    int ele_small,position,j;  
    ele_small = myarray[i];  
    position = i;  
    for(j=i+1;j<10;j++)  
    {  
        if(myarray[j]<ele_small)  
        {  
            ele_small = myarray[j];  
            position=j;  
        }  
    }  
    return position;  
}