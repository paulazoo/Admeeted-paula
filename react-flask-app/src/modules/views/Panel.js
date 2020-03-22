import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from "../components/Typography";
import Paper from "../components/Paper";

const styles = theme => ({
    paper: {
        textAlign: 'center',
        color: theme.palette.text.secondary,
    }
});

function Panel(props) {
    const { title, children, classes } = props;

    return (
        <div>
            <Typography variant='h6'>
                {title}
            </Typography>
            <Paper className={classes.paper}>
                {children}
            </Paper>
        </div>

    )
}

Panel.propTypes = {
    children: PropTypes.node.isRequired,
    title: PropTypes.string.isRequired,
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Panel);