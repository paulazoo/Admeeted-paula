import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const styles = theme => ({
    background: {
        backgroundColor: '#cfe8fc',
        height: '60vh',
        width: '40vw',
    },
});

function PanelLayout(props) {
    const { children, classes } = props;

    return (
      <Container className={classes.background}>
          {children}
      </Container>
    );
}

PanelLayout.propTypes = {
    children: PropTypes.node.isRequired,
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(PanelLayout);