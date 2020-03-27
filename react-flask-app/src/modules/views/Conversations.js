import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '../components/Typography';
import MainLayout from "../layouts/MainLayout";
import Grid from '@material-ui/core/Grid';
import Paper from '../components/Paper';
import Container from '@material-ui/core/Container';
import PanelLayout from './PanelLayout';
import Panel from "./Panel";
import PanelList from "./PanelList";
import Loading from "./Loading";
import CardList from '../components/CardList';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    upcomingRoot: {
        height: '100%'
    },
    availRoot: {
        height: '100%'
    }
});

function Conversations({ data, currentlySending, classes }) {
    const upcomingText = 'Your upcoming conversations';
    const availText = 'Your available conversations';

    const upcomingConvos = data.upcomingConvos;
    const availConvos = data.availConvos;

    const maxItems = 10;

    return(
        <div>
            {!currentlySending ? <MainLayout>
            <Grid container className={classes.root} spacing={4}>
                <Grid item
                    lg={6}
                    sm={6}
                    xl={6}
                    xs={12}
                >
                    <CardList title={upcomingText} data={upcomingConvos} maxItems={maxItems} className={classes.upcomingRoot}/>
                    {/*<PanelLayout>*/}
                    {/*    <Panel title={upcomingText}>*/}
                    {/*        <PanelList data={upcomingConvos}/>*/}
                    {/*    </Panel>*/}
                    {/*</PanelLayout>*/}
                </Grid>
                <Grid item
                    lg={6}
                    sm={6}
                    xl={6}
                    xs={12}
                >
                    <CardList title={availText} data={availConvos} maxItems={maxItems} className={classes.availRoot}/>
                    {/*<PanelLayout>*/}
                    {/*    <Panel title={availText}>*/}
                    {/*        <PanelList data={availConvos}/>*/}
                    {/*    </Panel>*/}
                    {/*</PanelLayout>*/}
                </Grid>
            </Grid>
        </MainLayout> : <Loading/>}
        </div>
    );
}

Conversations.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Conversations);