#include <string>
// Returns the string read in a zigzag pattern, for numRows = 3 and s = "abcabcabc":
// 1 -> a b c 
// 2 -> bacb
// 3 -> c a
// abcbacbca is the result 
//
std::string convert(std::string s, int numRows) 
{
    if(numRows==1)
    return s;
    
    std::string ans="";
    int x=(numRows-2)*2+2;
    int diagonal=numRows-2;

    for(int i=0;i<s.size();i=i+x)
    ans+=s[i];

    for(int i=1;i<=numRows-2;i++)
    { 
        int m=0;
        if(i<s.size())
        ans+=s[i];
        while(m+i<s.size())
        {
        m+=x-2*i;
        if(m+i>=s.size())
        break;
        ans+=s[i+m];
        m+=2*i;
        if(m+i>=s.size())
        break;
        ans+=s[i+m];
        }
    }
    for(int i=numRows-1;i<s.size();i=i+x)
    ans+=s[i];
    return ans;  
}