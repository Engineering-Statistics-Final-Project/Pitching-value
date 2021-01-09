#include <bits/stdc++.h>
#include <cstring>
#include <string>
using namespace std;

int main() {
    cin.tie(0), ios::sync_with_stdio(0);
    
    string str  = "DATA/";
    string str2 = ".txt";
    
    for(int i=1995;i<=2019;i++){
        string team_name = str+to_string(i)+str2;
        vector<string> team;
        map<string,string> rec;

        fstream FILE_NAME;
        FILE_NAME.open(team_name,ios::in);
        string tmp;
        while(getline(FILE_NAME,tmp)){
            string team_tmp_name;
            for(int i=1;i<tmp.length();i++){
                if(tmp[i]=='"')break;
                team_tmp_name += tmp[i];
            }
            team.push_back(team_tmp_name);
            rec[team_tmp_name] = tmp;
        }
        FILE_NAME.close();

        fstream FILE_NAME2;
        FILE_NAME2.open(team_name,ios::out);
        for(auto &t:rec){
            for(int j=0;j<t.second.length();j++){
                if(t.second[j]!='$')FILE_NAME2<<t.second[j];
            }
            FILE_NAME2<<"\n";
        }
        FILE_NAME2.close();
    }

    
    
    return 0;
}