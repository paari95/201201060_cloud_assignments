#include<cstdio>
#include<iostream>
#include<fstream>

using namespace std;


int main()
{
	ifstream fs("32_bit.asm");
	ofstream os("gen64.s");
	string ret;
	int i,j,k;
	while(getline(fs,ret))
	{
		string overall="";
		for(i=0;i<ret.size();i++)
		{
			string str="";
			for(j=i;ret[j]==' ';j++);
			for(j;j<ret.size() && ret[j]!=' ';j++)
			{
				str=str+ret[j];
			}
			i=j;
			if(str=="eax,4")
				str="rax,1";
			else if(str=="ebx,1")
				str="rdi,1";
			else if(str=="eax,1")
				str="rax,60";
			else if(str=="ebx,0")
				str="rdi,0";
			string over="";
			for(j=0;j<str.size();j++)
			{
				string loc="";
				for(k=j;k<str.size() && str[k]!=',';k++)
					loc=loc+str[k];
				j=k;
				if(loc=="ecx")
					loc="rsi";
				else if(loc=="edx")
					loc="rdi";
				over=over+loc;
				if(j!=str.size())
					over=over+',';
				
			}
			if(i>=ret.size())
				overall=overall+over;
			else
				overall=overall+over+' ';
		}
		cout<<overall<<endl;
		if(overall=="int 80h" || overall=="int 80h ")
			overall="syscall";
		os<<overall<<endl;
	}
	return 0;
}
