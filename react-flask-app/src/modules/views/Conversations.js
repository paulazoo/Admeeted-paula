import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '../components/Typography';
import ProductHeroLayout from "./ProductHeroLayout";
import Grid from '@material-ui/core/Grid';
import Paper from '../components/Paper';
import Container from '@material-ui/core/Container';
import PanelLayout from './PanelLayout';
import Panel from "./Panel";
import PanelList from "./PanelList";

const styles = theme => ({
    background: {
        backgroundColor: '#7fc7d9', // Average color of the background image.
        backgroundPosition: 'center',
    },
    root: {
        flexGrow: 1,
    },
});

function Conversations(props) {
    const { classes } = props;
    const upcomingText = 'Your upcoming conversations';
    const availText = 'Your available conversations';

    return(
        <ProductHeroLayout backgroundClassName={classes.background}>
            <Grid container className={classes.root} spacing={4}>
                <Grid item xs={12} sm={8} md={6}>
                    <PanelLayout>
                        <Panel title={upcomingText}>
                            <PanelList/>
                        </Panel>
                    </PanelLayout>
                </Grid>
                <Grid item xs={12} sm={8} md={6}>
                    <PanelLayout>
                        <Panel title={availText}>
                            <PanelList/>
                        </Panel>
                    </PanelLayout>
                </Grid>
            </Grid>
        </ProductHeroLayout>
    );
}

Conversations.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Conversations);