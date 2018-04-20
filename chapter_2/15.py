# coding: utf-8
# Your code here!

# coding: utf-8

def main():
    nums = [ 8, 3, 1, 2, 5, 4, 7, 6 ]
    group = { 2, 3, 5, 7 }
    
    l = sort_1(nums, group)
    print(nums)  # [8, 3, 1, 2, 5, 4, 7, 6]
    print(l)     # [2, 3, 5, 7, 1, 4, 6, 8]
    
    r2, l2 = sort_2(nums, group)
    print(r2, l2)
    #False [2, 3, 5, 7, 1, 4, 6, 8]
    
    r3, l3 = sort_3(nums, group)
    print(r3, l3)
    #True [2, 3, 5, 7, 1, 4, 6, 8]

def sort_1(values, group):
    def helper(x):
        #クロージャ(closure) : 定義されたスコープの変数を参照する関数→helper関数がsort_priorityの引数にアクセスできる
        if x in group:
            return (0, x)
        return (1, x)
    return sorted(values, key=helper)
    

def sort_2(values, group):
    found = False #スコープ：sort_2
    def helper(x):
        if x in group:
            found = True #スコープ：helper
            return (0, x)
        return (1, x)
    return found, sorted(values, key=helper) # foundは常にFalseを返す
    # pythonインタープリタによる変数の参照順
    # 1. 現在の関数のスコープ
    # 2. 外側のスコープ（ex, 他の関数の中）
    # 3. コードを含むモジュールのスコープ
    # 4. 組み込みスコープ
    # 1~4に当てはまらない場合、NameError
    # visual studio codeではunusedの警告が表示される


def sort_3(values, group):
    found = False 
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    l = sorted(values, key=helper)
    return found, l


if __name__ == '__main__':
    main()