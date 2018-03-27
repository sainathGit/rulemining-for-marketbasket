#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <string>

#define htable map<vector<int>, int>
using namespace std;

void getinput(vector<vector<int>> &db) {

	int n;
	cin >> n;
	string line;
	getline(cin ,line);

	while(n--) {
		getline(cin, line);
		istringstream iss(line);
		vector<int> t;

		int temp;
		while (iss >> temp) 
			t.push_back(temp);
		
		db.push_back(t);	
	}
return;
}


void find_frequent1(vector<vector<int>> &db, htable &l) {

	for (int i = 0; i < db.size(); ++i)
		{
			for (int j = 1; j < db[i].size(); ++j)
			{
				vector<int> temp;
				temp.push_back(db[i][j]);
				if (l.find(temp) == l.end()) 
					l[temp] = 1;
				else
					l[temp]++;
			}
		}	
}



int main(int argc, char const *argv[])
{
	
	map<vector<int>, int> c[5], l[5];

	vector<vector<int>> db;
	getinput(db);

	find_frequent1(db, l[0]);

	htable :: iterator it;
	for (it = l[0].begin(); it != l[0].end(); ++it)
		cout << "key : " << it->first[0] << "  value : " << it->second << endl;
	


	return 0;
}