'''
Non local scope
'''

# E.g 1),
# Non local scope
# Global Scope
def washingmachine():
    # Enclosing Scope
    clothes = 'Clean and wet'
    def dryclean():
        #Local Scope
        nonlocal clothes
        clothes = 'Dry and Clean'
        print(clothes)
    dryclean()
    print(clothes)
washingmachine()