from Storm import Storm
from blizzard import Blizzard
from hurricane import Hurricane
 
storm = Storm("test_1",45)

if isinstance(storm, Blizzard) or isinstance(storm, Hurricane):
    print('true')
    ans = storm.calculate_classification()
    print(ans)
else:
    print('false')
    ans = storm.calculate_classification()
    print(ans)
