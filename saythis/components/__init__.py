import os

def whereis_exe(program):
    ''' Tries to find the program on the system path.
        Returns the path if it is found or None if it's not found.
    '''
    for path in os.environ.get('PATH', '').split(':'):
        if os.path.exists(os.path.join(path, program)) and \
            not os.path.isdir(os.path.join(path, program)):
            return os.path.join(path, program)
    return None