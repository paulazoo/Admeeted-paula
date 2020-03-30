import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import MainLayout from "../layouts/MainLayout";
import {Divider, Typography} from "@material-ui/core";
import Loading from "./Loading";
import Grid from "@material-ui/core/Grid";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardHeader from "@material-ui/core/CardHeader";
import AccountDetails from "../components/AccountDetails";
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';

const styles = theme => ({
    gridList: {
        width: '100%',
        height: 130
    },
    card: {
        width: '100%'
    },
    intro: {
        padding: theme.spacing(4)
    },
    image: {
        height: 64,
        width: 64
    }
})

function Welcome ({ profile, currentlySending, setProfile, classes }) {
    const stepOneTitle = "Step One: Complete Your Profile";
    const stepOneSubtitle = "Edit and save your profile details.";
    const stepTwoTitle = "Step Two: Join an Organization";
    const stepTwoSubtitle = "Click the search icon above to find an organization to join.";
    const stepThreeTitle = "Step Three: Share the Love!";
    const stepThreeSubtitle = "Spread the word so we can bring this to more people.";

    const image_srcs = [
        'https://www.harvard.edu/sites/default/files/user13/harvard_shield.png',
        'https://upload.wikimedia.org/wikipedia/commons/f/f1/Princetonshieldlarge.png'
    ]

    return (
        <div>
            {!currentlySending ? <MainLayout>
            <Grid container spacing={4}>
                <Grid item md={12}>
                    <Card className={classes.card}>
                        <CardContent>
                            <Typography align={"center"} variant={"h1"} className={classes.intro}>
                                Welcome
                            </Typography>
                            <Typography align={"center"} variant={"h5"}>
                                We noticed it is your first time here! Let us get you set up.
                            </Typography>
                        </CardContent>
                    </Card>
                </Grid>
                <Grid item md={6}>
                    <AccountDetails title={stepOneTitle} subtitle={stepOneSubtitle} profile={profile} setProfile={setProfile}/>
                </Grid>
                <Grid item md={6}>
                    <Card className={classes.card}>
                        <CardHeader title={stepTwoTitle} subheader={stepTwoSubtitle}/>
                        <CardContent>
                            Once you join an organization, you will be able to view and join upcoming events where you can meet other people
                            who share your interests.
                        </CardContent>
                        <Divider/>
                        <CardHeader title={stepThreeTitle} subheader={stepThreeSubtitle}/>
                        <CardContent>
                            We are a team of college-bound students hoping to bring together this year's pre-first year class amidst an
                            unprecedented global crisis. If you would like to contribute or give feedback, you can contact us at
                            admeeted2.0@gmail.com - thanks!
                        </CardContent>
                    </Card>
                </Grid>
            </Grid>
        </MainLayout> : <Loading/>}
        </div>
    )
}

export default withStyles(styles)(Welcome);