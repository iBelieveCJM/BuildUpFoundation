#include<cstddef>
/*
 不考虑重叠情况
*/
void* _memcpy(void *dst, const char *src, size_t size)
{
    if(dst==nullptr || src==nullptr){
        return nullptr;
    }
    char* pdst = (char*)dst;
    const char* psrc = (const char*)src;
    while(size--){
        *pdst++ = *psrc++;
    }
    return dst;
}

/*
 考虑重叠情况
*/
void* _memmove(void *dst, const char *src, size_t size)
{
    if(dst==nullptr || src==nullptr){
        return nullptr;
    }
    char* pdst = (char*)dst;
    const char* psrc = (const char*)src;
    if( psrc<pdst && pdst<(psrc+size) ){
        pdst = pdst + size-1;
        psrc = psrc + size-1;
        while(size--){
            *pdst-- = *psrc--;
        }
    }else{
        while(size--){
            *pdst++ = *psrc++;
        }
    }
    return dst;
}