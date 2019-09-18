// 单例模式
// 要点：
//   1. 全局只有一个实例
//   2. 线程安全
//   3. 禁止复制和拷贝
//   4. 用户通过接口获取实例：使用 static 类成员函数

/* 有缺陷的懒汉式
懒汉式(Lazy-Initialization) 的方法是直到使用时才实例化对象
优点：不被调用就不会占用内存
问题：
  1. 线程不安全：当多线程获取单例时有可能引发竞态条件（解决办法：加锁）
  2. 内存泄漏：只负责 new 对象，但没有 delete 对象（解决办法：使用共享指针）
*/
class Singleton{
private:
    Singleton(){};         // 私有化默认构造函数，只允许内部创建
    Singleton(Singleton&)=delete;                  // 禁止拷贝
    Singleton& operator=(const Singleton&)=delete; // 禁止赋值
private:
    static Singleton* m_instance_ptr;
public:
    static Singleton* get_instance(){
        if(m_instance_ptr==nullptr){ // 线程不安全
            m_instance_ptr = new Singleton;
        }
        return m_instance_ptr;
    }
};
Singleton* Singleton::m_instance_ptr = nullptr;


/* 改进的懒汉式：线程安全、内存安全
优点：
  1. 加锁达到线程安全；这里使用了两个 if 语句的技术称为双检锁，
     避免了每次调用 get_instance 都加锁，锁的开销有点大
  2. 基于 shared_ptr，避免了内存泄漏
问题：
  1. 强制用户使用智能指针
  2. 在某些平台，双检锁会失效
*/
#include<memory> // shared_ptr
#include<mutex>  // mutex
class Singleton{
public:
    typedef std::shared_ptr<Singleton> Ptr;
private:
    Singleton(){};         // 私有化默认构造函数，只允许内部创建
    Singleton(Singleton&)=delete;                  // 禁止拷贝
    Singleton& operator=(const Singleton&)=delete; // 禁止赋值
private:
    static Ptr m_instance_ptr;
    static std::mutex m_mutex;
public:
    static Ptr get_instance(){
        // double checked lock
        if(m_instance_ptr==nullptr){
            std::lock_guard<std::mutex> lk(m_mutex);
            if(m_instance_ptr==nullptr){
                m_instance_ptr = new Singleton;
            }
        }
        return m_instance_ptr;
    }
};
Singleton* Singleton::m_instance_ptr = nullptr;


/* Magic staic
使用静态局部变量来达到只执行一次
优点：
  1. 通过静态局部变量的特性保证了线程安全
  2. 不需要使用 shared_ptr
要点：
  1. get_instance 返回引用 Single&；
     若返回指针，无法避免用户提前销毁对象
*/
class Singleton{
private:
    Singleton(){};         // 私有化默认构造函数，只允许内部创建
    Singleton(Singleton&)=delete;                  // 禁止拷贝
    Singleton& operator=(const Singleton&)=delete; // 禁止赋值
public:
    static Singleton& get_instance(){
        static Singleton instance;  // 静态局部变量，只执行一次
        return instance;
    }
};