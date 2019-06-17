class Shields:
    '''
    Holds the Data for getting the Shields.
    '''
    shields = {
        'appveyor': {
            'appveyor': '/appveyor/ci/{user}/{repo}.svg',
            'appveyor': '/appveyor/ci/:user/:repo/:branch.svg',
        }
    }

    def get_shield(self, thing_name=None):
        '''

        '''
        if thing_name.lower() == 'appveyor':
