import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import AppForm from './AppForm';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';

const styles = theme => ({
    root: {
        display: 'flex',
        backgroundImage: 'url(https://i.pinimg.com/originals/bc/1e/88/bc1e8884b0c4cb638753ba953e102334.jpg)',
        // backgroundRepeat: 'no-repeat',
        backgroundSize: 'fill',
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
                            width="640" height="2039" frameBorder="0" marginHeight="0" marginWidth="0">Loading…
                        </iframe>
                    </Box>
                </Container>
            </div>
        </React.Fragment>
    );
}

export default withStyles(styles)(StaticGoogleForm);