#include<cstring>
/*
 version1: 没有考虑重叠情况
*/
char* _strcpy(char* dst, const char* src)
{
    if(dst==nullptr || src==nullptr){
        return nullptr;
    }
    char* ret = dst;
    while( (*dst++ = *src++) != '\0' );
    return ret;
}

char* _strcpy(char* dst, const char* src)
{
    if(dst==nullptr || src==nullptr){
        return nullptr;
    }
    char* ret = dst;
    memcpy(dst, src, strlen(src)+1);
    return ret;
}

/*
 version1: 考虑重叠情况
*/
char* _strcpy(char* dst, const char* src)
{
    if(dst==nullptr || src==nullptr){
        return nullptr;
    }
    char* ret = dst;
    int size = strlen(src)+1;
    if( src<dst && dst<(src+size) ){
        dst = dst + size-1;
        src = src + size-1;
        while(size--){
            *dst-- = *src--;
        }
    }else{
        while(size--){
            *dst++ = *src++;
        }
    }
    return ret;
}