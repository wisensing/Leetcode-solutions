class Solution(object):
    def groupAnagrams(self, strs):
        '''
        len_strs = len(strs)
        if len_strs < 2:
            return [strs]
        new_list = []
        i = 0 
        
        while len(strs) > 1:
            str_temp = sorted(strs[0])
            temp_list = []
            temp_list.append(strs[0])
            strs[0]=0
            
            for j in range(1,len(strs)):
                str_temp_2 = sorted(strs[j])
                if str_temp == str_temp_2:
                    temp_list.append(strs[j])
                    strs[j] = 0

            new_list.append(temp_list)
            strs = [str for str in strs if str != 0 ]
        if len(strs) == 1 and strs[0] != 0:
                new_list.append(strs)
       
        return new_list
        '''
                      
        mp = defaultdict(list)
        
        for str in strs:
            sorted_str = ''.join(sorted(str))
            
            mp[sorted_str].append(str)
            
        return mp.values()
    
 
    
    
    
    
    