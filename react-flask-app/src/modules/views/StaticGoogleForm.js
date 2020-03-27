import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import AppForm from './AppForm';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';

const styles = theme => ({
    root: {
        display: 'flex',
        backgroundImage: 'url(https://upload.wikimedia.org/wikipedia/commons/c/c7/Memorial_Hall_%28Harvard_University%29_-_facade_view.JPG)',
        // backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
      }
});

function StaticGoogleForm ({ classes }) {
    return (
        <React.Fragment>
            <div className={classes.root}>
                <Container maxWidth='sm'>
                    <Box mt={7} mb={12}>
                        <iframe
                            src="https://docs.google.com/forms/d/e/1FAIpQLScrrI4c-SRt6blejIZLADnBDt98UUg-2pMxrfMiChnDykhkGw/viewform?embedded=true"
                            width="640" height="1500" frameBorder="0" marginHeight="0" marginWidth="0">Loading…
                        </iframe>
                    </Box>
                </Container>
            </div>
        </React.Fragment>
    );
}

export default withStyles(styles)(StaticGoogleForm);