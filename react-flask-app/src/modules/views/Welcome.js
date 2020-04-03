import React, {useState} from 'react';
import { withStyles } from '@material-ui/core/styles';
import MainLayout from "../layouts/MainLayout";
import {Button, CardActions, Divider, TextField, Typography} from "@material-ui/core";
import Loading from "./Loading";
import Grid from "@material-ui/core/Grid";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardHeader from "@material-ui/core/CardHeader";
import AccountDetails from "../components/AccountDetails";
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import {Autocomplete} from "@material-ui/lab";

const styles = theme => ({
    root : {
        width: '50vw'
    },
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
    form: {
        marginTop: theme.spacing(4)
    }
})

function Welcome ({ profile, allMajors, allOrganizations, allInterests, currentlySending, setProfile, classes, history }) {
    const [view, setView] = useState(false);

    const stepOneTitle = "Step One: Complete Your Profile";
    const stepOneSubtitle = "Edit and save your profile details.";
    const stepTwoTitle = "Step Two: Join an Organization";
    const stepTwoSubtitle = "Search below for an organization to begin your exploration.";
    const stepThreeTitle = "Step Three: Share the Love!";
    const stepThreeSubtitle = "Spread the word so we can bring this to more people.";

    function setViewAndProfile(new_data) {
        setProfile(new_data);
        setView(true);
    }

    const [values, setValues] = useState({
        query: '',
        redirect: false,
        error: false
    });

    const handleSubmit = event => {
        const organizations = allOrganizations.filter((e) => e.displayName === values.query);
        if (organizations.length > 0) {
            history.push(`/organization/${organizations[0].id}`)
        //     setValues({
        //     ...values,
        //     redirect: organizations[0].id
        // })
        }
        else {
            setValues({
                ...values,
                error: true
            })
        }
    }

    const handleChange = (event, value) => {
        setValues({
            ...values,
            query: value,
            error: false
        })
    }

    return (
        <div>
            {!currentlySending ? <MainLayout>
            <Grid container spacing={4} className={classes.root}>
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
                {!view ? <Grid item md={12}>
                    <AccountDetails
                        title={stepOneTitle}
                        subtitle={stepOneSubtitle}
                        allMajors={allMajors}
                        allInterests={allInterests}
                        profile={profile}
                        setProfile={setViewAndProfile}
                    />
                </Grid> : <Grid item md={12}>
                    <Card className={classes.card}>
                        <CardHeader title={stepTwoTitle} subheader={stepTwoSubtitle}/>
                        <CardContent>
                            Once you join an organization, you will be able to view and join upcoming events where you can meet other people
                            who share your interests.
                            <Autocomplete
                                className={classes.form}
                                variant="outlined"
                                options={allOrganizations}
                                getOptionLabel={(option) => option.displayName}
                                required
                                renderInput={(params) => <TextField
                                    {...params}
                                    label={values.error ? "Invalid organization name" : "Organization name"}
                                    variant="outlined"
                                    error={values.error}
                                />}
                                onInputChange={handleChange}
                            />
                        </CardContent>
                        {/*<Divider/>*/}
                        {/*<CardHeader title={stepThreeTitle} subheader={stepThreeSubtitle}/>*/}
                        {/*<CardContent>*/}
                        {/*    We are a team of college-bound students hoping to bring together this year's pre-first year class amidst an*/}
                        {/*    unprecedented global crisis. If you would like to contribute or give feedback, you can contact us at*/}
                        {/*    admeeted2.0@gmail.com - thanks!*/}
                        {/*</CardContent>*/}
                        <CardActions>
                            <Button
                                color="primary"
                                variant="contained"
                                onClick={handleSubmit}
                            >
                                    Go!
                            </Button>
                        </CardActions>
                    </Card>
                </Grid>}
            </Grid>
        </MainLayout> : <Loading/>}
        </div>
    )
}

export default withStyles(styles)(Welcome);