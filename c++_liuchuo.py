C语⾔言的输入输出（ scanf 和 printf ）⽐C++快，那么就可以在使⽤用C++刷算法同时使⽤用 scanf 和 printf 提⾼高代码运⾏行行效率

C++中的string比C语言中的char数组好用得多

写算法题看官方文档必不可少

在解决⼀一些较为简单的PAT⼄乙级题⽬目的时候（例例如⼀一些时间复杂度限制不不严格的题目）， cin 、 cout 输⼊入输出⾮非常⽅方便

名称空间using namespace std的解释
    因为不同厂商定义的名称空间可能会彼此冲突，所以我们要指明具体用的哪一个名称空间，一般都用“std”。
    就和return 0一样必须有
    如cin、cout就是std中的
        std::cin >> n;
        std::cout << "hello, liuchuo" << n + 1 << endl;#也可以这么代替，但是不方便

cin和cout输入输出
    在头文件iostream中

    不管 n 是 double 还是 int 或者是 char 类型，只⽤写 cin >> n; 和 cout << n; 这样简单的语句就好，不不⽤用像C语言中需要根据 n 的类型对应地写 %lf 、 %d 、 %c 这样麻烦

    endl 和 “\n”一个意思，全程“end of line”
    cout << "hello, ⼩小可爱～\n";
    cout << n << endl;

    用 cin 读入字符串的时候，是以空格为分隔符的，如果想要读入一整行的字符串串，就需要用 getline

C++的头文件
    C++的头⽂文件⼀一般是没有像C语⾔言的 .h 这样的扩展后缀的，⼀般情况下C语⾔言⾥里里⾯面的头⽂文件去掉 .h 然后在前⾯面加个 c 就可以继续在C++⽂文件中使⽤用C语⾔言头⽂文件中的函数啦

    include <cmath> // 相当于C语⾔言⾥里里⾯面的#include <math.h>
    include <cstdio> // 相当于C语⾔言⾥里里⾯面的#include <stdio.h>
    include <cctype> // 相当于C语⾔言⾥里里⾯面的#include <ctype.h>
    include <cstring> // 相当于C语⾔言⾥里里⾯面的#include <string.h>

C++的变量声明
    C语言必须在函数开头定义变量，C++只要在变量使用之前定义即可

    ⼀般C语言里面会在 for 循环的外面定义 i 变量，但是C++⾥面可以在 for 循环内部定义

C++特有的bool变量
    非零值即为true

C++特有的const定义变量
    用于取代C语言中的#define
    const独有的好处是可以定义常量的类型
    const int a = 99999999;

C++中很好用的string类
    以前⽤用 char[] 的方式处理字符串很繁琐，现在有了string 类，定义、拼接、输出、处理都更加简单啦

    不过 /*/string 只能⽤用 cin 和 cout 处理，无法用 scanf 和 printf 处理  如果想用printf输出string，得加⼀一个.c_str()  /*/

    string s = "hello world"; // 赋值字符串
    string s2 = s;
    string s3 = s + s2; // 字符串拼接直接用+号就可以   /*/
    string s4;
    cin >> s4; // 读⼊入字符串
    cout << s; // 输出字符串


    /*/s的长度可以用 s.length() 获取～（有几个字符就是长度多少，不存在 char[] 里面的什什么末尾的结束符之类的～）
    string s; // 定义一个空字符串s
    getline(cin, s); // 读取一行的字符串，包括空格*/*
    cout << s.length(); // 输出字符串s的长度

    /*/string 中还有个很常用的函数叫做 substr ，作用是截取某个字符串中的子串，用法有两种形式：
    
    string s2 = s.substr(4); // 表示从下标4开始一直到结束
    string s3 = s.substr(5, 3); // 表示从下标5开始， 3个字符


C++的结构体struct和C语言的结构体的区别
    定义好结构体 stu 之后，使用这个结构体类型的时候， C语言需写关键字 struct ，⽽而C++里面可以省略不写
    struct stu {
    int grade;
    float score;
    };
    struct stu arr1[10]; // C语言里面需要写成struct stu
    stu arr2[10];// C++⾥面不用写struct，直接写stu就好了～/*/

C++引用&和传值的区别/*/
    这个引用符号 & 要和C语言里面的取地址运算符 & 区分开来，他们没有什么关系， C++里面的引用是指在变量名之前加⼀一个 & 符号

    比如在函数传入的参数中 int &a ，那么对这个引用变量 a 做的所有操作都是直接对传入的原变量进行的操作，并没有像原来 int a 一样只是拷贝一个副本（传值）

    void func(int &a) { 
        // 传入的是n的引用，相当于直接对n进行了操作，只不过在func函数中换了个名字叫a
    a = 99;
    }
    int main() {
    int n = 0;
    func(n); // n由0变成了了99
    }

    void func(int a) {
        // 传入的是0这个值，并不会改变main函数中n的值
    a = 99;
    }
    int main() {
    int n = 0;
    func(n);// 并不会改变n的值， n还是0
    }

容器：
vector
    动态数组/不定长数组
    它能够在运行阶段设置数组的长度，在末尾增加新的数据、在中间插入新的值、长度任意被改变

    可以一开始不定义大小，之后用resize方法分配大小
    也可以一开始就定义大小，之后对它插入删除动态改变她的大小

    不管是在main函数还是全局中定义，她都能够直接将所有的值初始化为0（不用显示地写出来，默认所有的元素为0）

    vector<int> v(10); // 直接定义⻓长度为10的int数组，/*/默认这10个元素值都为0/*/
    // 或者
    vector<int> v1;
    v1.resize(8); //先定义⼀一个vector变量量v1，然后将⻓长度resize为8，默认这8个元素都是0/*/
    // 在定义的时候就可以对vector变量量进⾏行行初始化
    vector<int> v3(100, 9);// 把100⻓长度的数组中所有的值都初始化为9/*/
    // 访问的时候像数组⼀一样直接⽤用[]下标访问即可/*/～(也可以⽤用迭代器器访问，下⾯面会讲～)
    v[1] = 2;
    cout << v[0];


    vector<int> b(15); // 定义的时候指定vector的⼤小，默认b⾥面元素都是0
    vector<int> c(20, 2); // 定义的时候指定vector的⼤小并把所有的元素赋一个指定的值
    c.end() 指向容器器的最后一个元素的后一个位置/*/


set 集合
    一个set里面的各元素元素是各不相同的，而且set会按照元素进行从小到大排序
    
    常用用法:
        #include <iostream>
        #include <set>
        using namespace std;
        int main() {
        set<int> s; // 定义一个空集合s/*/
        s.insert(1); // 向集合里面插⼊一个1/*/
        cout << *(s.begin()) << endl; // 输出集合s的第⼀一个元素 (前⾯面的星号表示要对指针取值)
        for (int i = 0; i < 6; i++) {
            s.insert(i); // 向集合s⾥里里⾯面插⼊入i
        }
        for (auto it = s.begin()/*/; it != s.end(); it++) { // ⽤用迭代器遍历集合s⾥面的每一个元素
            cout << *it << " ";
        }
        cout << endl << (s.find(2) != s.end()/*/) << endl; // 查找集合s中的值，如果结果等于s.end()表示未找到 (因为s.end()表示s的最后一个元素的下一个元素所在的位置)
        cout << (s.find(10) != s.end()) << endl; // s.find(10) != s.end()表示能找到10这个元素
        s.erase(1); // 删除集合s中的1这个元素/*/
        cout << (s.find(1) != s.end()) << endl; // 这时候元素1就应该找不不到啦～
        return 0;
        }
        find auto erase begin() end() /*/

map映射
    map 会按照键值对的键 key 进行排序
    键值对   如map<string, int> m;
    常用用法    
        #include <iostream>
        #include <map>
        #include <string>
        using namespace std;
        int main() {
        map<string, int> m; // 定义一个空的map m，键是string类型的，值是int类型的
        m["hello"] = 2; // 将key为"hello", value为2的键值对(key-value)存⼊入map中
        cout << m["hello"] << endl; // 访问map中key为"hello"的value, 如果key不不存在，则返回0
        cout << m["world"] << endl;
        m["world"] = 3; // 将"world"键对应的值修改为3
        m[","] = 1; // 设⽴立⼀一组键值对，键为"," 值为1
        // ⽤用迭代器器遍历，输出map中所有的元素，键⽤用it->first获取，值⽤用it->second获取
        for (auto it = m.begin(); it != m.end(); it++) {
        cout << it->first << " " << it->second << endl;
        }
        // 访问map的第⼀一个元素，输出它的键和值
        cout << m.begin()->first << " " << m.begin()->second << endl;
        // 访问map的最后⼀一个元素，输出它的键和值/*/
        cout << m.rbegin()->first << " " << m.rbegin()->second << endl;*/*
        // 输出map的元素个数
        cout << m.size() << endl;/*/
        return 0;
        }

        first second/*/

stack/*/
    常用用法
        #include <iostream>
        #include <stack>
        using namespace std;
        int main() {
        stack<int> s; // 定义一个空栈s
        for (int i = 0; i < 6; i++) {
        s.push(i); // 将元素i压⼊入栈s中
        }
        cout << s.top() << endl; // 访问s的栈顶元素
        cout << s.size() << endl; // 输出s的元素个数
        s.pop(); // 移除栈顶元素
        return 0;
        }

queue
    常用用法
        #include <iostream>
        #include <queue>
        using namespace std;
        int main() {
        queue<int> q; // 定义一个空队列q
        for (int i = 0; i < 6; i++) {
        q.push(i); // 将i的值依次压入队列q中
        }
        cout << q.front() << " " << q.back() << endl; // 访问队列的队首元素和队尾元素/*/
        cout << q.size() << endl; // 输出队列的元素个数
        q.pop(); // 移除队列的队首元素
        return 0;
        }
    stack中是top，queue中是front和back/*/
    stack中pop移除栈顶元素，queue中pop移除队列的队首元素/*/

unordered_map和unordered_set
     #include <unordered_map> 
     #include<unordered_set>
     unordered_map 和 map （或者 unordered_set 和 set ）的区别是， map 会按照键值对的键 key 进行排序/*/（ set ⾥面会按照集合中的元素⼤小进⾏行行排序，从小到大顺序），而 unordered_map （或者 unordered_set ）省去了这个排序的过程，如果偶尔刷题时候⽤用 map 或者 set 超时了/*/，可以考虑⽤用 unordered_map （或者 unordered_set ）缩短代码运行时间、提高代码效率～⾄于用法和map 、 set 是⼀一样的～/*/



C++的位运算biset
    biset处理二进制位非常方便，在leetcodeOJ中经常用到
    #include <iostream>
    #include <bitset>
    using namespace std;
    int main() {
    bitset<5> b("11"); //5表示5个二进位    00011 /*/
    // 初始化⽅方式：
    // bitset<5> b; 都为0
    // bitset<5> b(u); u为unsigned int，如果u = 1，则输出b的结果为00001
    // bitset<8> b(s); s为字符串串，如"1101"，则输出b的结果为00001101，在前⾯面补0
    // bitset<5> b(s, pos, n); 从字符串串的s[pos]开始， n位长度
    // 注意， bitset相当于⼀一个数组，但是它是从⼆进制的低位到高位分别为b[0]、 b[1]……的
    // 所以按照b[i]方式逐位输出和直接输出b结果是相反的/*/
    cout << b << endl; // 如果bitset<5> b("11"); 则此处输出00011(即正常二进制顺序)
    for(int i = 0; i < 5; i++)
        cout << b[i]; // 如果bitset<5> b("11"); 则此处输出11000(即正常二进制顺序的倒序)
    /*/
    cout << endl << b.any(); //b中是否存在1的二进制位
    cout << endl << b.none(); //b中不存在1吗？
    cout << endl << b.count(); //b中1的二进制位的个数
    cout << endl << b.size(); //b中二进制位的个数
    cout << endl << b.test(2); //测试下标为2处是否二进制位为1
    b.set(4); //把b的下标为4处置1
    b.reset(); //所有位归零
    b.reset(3); //b的下标3处归零
    b.flip(); //b的所有二进制位逐位取反
    /*/
    unsigned long a = b.to_ulong();    //b转换为unsigned long类型
    return 0;
    }

sort函数
    在#include <algorithm>里面 /*/
    主要是对一个数组进行排序（ int arr[] 数组或者 vector 数组都行）
    vector 是容器，要用 v.begin() 和 v.end() 表示头尾
    而 int arr[] 用 arr 表示数组的首地址， arr+n 表示尾部

    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    bool cmp(int a, int b) { // cmp函数返回的值是bool类型
        return a > b; // 从大到⼩排列   /*/ 大于号从大到小   小于号从小到大
    }
    int main() {
    vector<int> v(10);
    for (int i = 0; i < 10; i++) {
        cin >> v[i];
    }
    sort(v.begin(), v.end());// 因为这里没有传入参数cmp，所以按照默认， v从小到大排列/*/
    int arr[10];
    for (int i = 0; i < 10; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + 10, cmp); // arr从大到小排列，因为cmp函数排序规则设置了了从大到小/*/
    return 0;
    }

C++中使用sort自定义cmp函数

    #include <iostream>
    using namespace std;
    struct stu { // 定义⼀一个结构体stu， number表示学号， score表示分数
        int number;
        int score;
    }
    bool cmp(stu a, stu b) { // cmp函数，返回值是bool，传⼊入的参数类型应该是结构体stu类型
        if (a.score != b.score) // 如果学⽣生分数不不同，就按照分数从大到小排列列
        return a.score > b.score;
        else // 如果学⽣生分数相同，就按照学号从小到大排列列
        return a.number < b.number;
    }
    // 有时候这种简单的if-else语句句我喜欢直接⽤用⼀一个C语⾔言⾥里里⾯面的三⽬目运算符表示～
    bool cmp(stu a, stu b) {
        return a.score != b.score ? a.score > b.score : a.number < b.number;
    }

    注意： sort 函数的 cmp 必须按照规定来写，即必须只是 > 或者 < ，比如： return a > b; 或者 return a < b; 而不能是 <= 或者 >= ，因为快速排序的思想中， cmp 函数是当结果为 false 的时候迭代器指针暂停开始交换两个元素的位置，当 cmp 函数 return a <= b 时，若中间元素前面的元素都比它小，⽽而后面的元素都跟它相等或者比它小，那么 cmp 恒返回 true ，迭代器指针会不断右移导致程序越界，发生段错误～


关于cctype头文件里的一些函数
    本质上来源于C语⾔言标准函数库中的头文件 #include<ctype.h> 
    可能平时我们判断⼀一个字符是否是字⺟母，可能会写：
    char c;
    cin >> c;
    if (c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z') {
    cout << "c is alpha";
    }
    但是在 cctype 中已经定义好了了判断这些字符应该所属的范围，直接引入这个头文件并且使⽤用里面的函数判断即可，无需⾃己手写（自己手写有时候可能写错或者漏写～）
    #include <iostream>
    #include <cctype>
    using namespace std;
    int main() {
    char c;
    cin >> c;0 
    if (isalpha(c)) {
    cout << "c is alpha";
    }
    return 0;
    }
    不仅能判断字母，还能判断数字、小写字母、大写字母等
    isalpha 字母（包括大写、小写）
    islower （小写字母）
    isupper （大写字母）
    isalnum （字母大写小写+数字）
    isblank （space和 \t ）
    isspace （ space 、 \t 、 \r 、 \n ）

    cctype 中除了了上面所说的用来判断某个字符是否是某种类型，还有两个经常用到的函数： tolower和 toupper
    char c = 'A';
    char t = tolower(c); // 将c字符转化为小写字符赋值给t，如果c本身就是小写字符也没有关系～
    cout << t; // 此处t为'a'


关于C++11的解释
    C++11是2011年年官⽅方为C++语⾔言带来的新语法新标准， C++11为C++语言带来了了很多好用的新特性，⽐比如 auto 、 to_string() 函数、 stoi 、 stof 、 unordered_map 、 unordered_set 之类的

    C++11里面很好用的auto声明
        auto 是C++11里面的新特性，可以让编译器根据初始值类型直接推断变量的类型。
        auto x = 100; // x是int变量
        auto y = 1.5; // y是double变量

        // 本来set的迭代器器遍历要这样写：
        for(set<int>::iterator it = s.begin(); it != s.end(); it++) {
        cout << *it << " ";
        }
        // 现在可以直接替换成这样的写法：
        for(auto it = s.begin(); it != s.end(); it++) {
        cout << *it << " ";
        }

    C++11特性中基于范围的for循环    
        基于范围（range-based）的for循环，这在遍历数组中的每一个元素时使用会比较简便
        int arr[4] = {0, 1, 2, 3};
        for (int i : arr)    
        //相当于 for (i = 0; i < arr.size(); i++) 
            cout << i << endl; // 输出数组中的每⼀一个元素的值，每个元素占据⼀行

        i 变量从数组的第一个元素开始，不断执行循环， i 依次表示数组中的每一个元素～注意，使用 int i 的方式定义时，该语句只能用来输出数组中元素的值，⽽不能修改数组中的元素，如果想要修改，必须使用 int &i 这种定义引用变量的方式～比如想给数组中的每一个元素都乘以 2 ，可以使用如下方式：

            int arr[4] = {0, 1, 2, 3};
            for (int &i : arr) // i为引⽤用变量量
                i = i * 2; // 将数组中的每⼀一个元素都乘以2， arr[4]的内容变为了了{0, 2, 4, 6}

        这种 for 循环方式不仅可以适用于数组，还适用于各种STL容器，比如 vector 、 set 等～加上面⼀节所讲的C++11里面很好用的 auto 声明，将 int 、 double 等变量类型替换成 auto ，用起来就更方便啦～

        // v是⼀一个int类型的vector容器
        for (auto i : v)
            cout << i << " ";
        // 上⾯面的写法等价于
        for (int i = 0; i < v.size(); i++)
            cout << v[i] << " ";
    
    C++11特性中的to_string
        to_string 最常用的就是把⼀个 int 型变量或者一个数字转为 string 类型的变量，当然也可以转 double 、 float 等类型的变量

        #include <iostream>
        #include <string>
        using namespace std;

        int main(){
            string s1 = to_string(123); // 将123这个数字转成字符串
            cout << s1 << endl;
            string s2 = to_string(4.5); // 将4.5这个数字转成字符串
            cout << s2 << endl;
            cout << s1 + s2 << endl; // 将s1和s2两个字符串拼接起来并输出
            printf("%s\n", (s1 + s2).c_str()); // 如果想用printf输出string，得加⼀一个.c_str()   /*/
            return 0;
        }

    C++11特性中的stoi、 stod
        使用 stoi 、 stod 可以将字符串 string 转化为对应的 int 型、 double 型量
        #include <iostream>
        #include <string>
        using namespace std;
        int main() {
            string str = "123.44";
            int a = stoi(str);
            cout << a;//输出123
            str = "123.44";
            double b = stod(str);
            cout << b;//输出123.44
            return 0;
        }
        不仅有stoi、 stod两种，相应的还有：
        stof (string to float)
        stold (string to long double)
        stol (string to long)
        stoll (string to long long)
        stoul (string to unsigned long)
        stoull (string to unsigned long long)







