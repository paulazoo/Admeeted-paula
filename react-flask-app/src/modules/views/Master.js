import React, {useState} from "react";
import Button from "@material-ui/core/Button";
import MainLayout from "../layouts/MainLayout";
import {
    Select,
    TextField,
    MenuItem,
    Card,
    CardHeader,
    CardContent,
    CardActions,
    Divider,
    InputLabel,
    FormControl,
    Typography,
    Grid
} from "@material-ui/core";
import { withStyles } from '@material-ui/core/styles';
import ReactJson from "react-json-view";
import Loading from "./Loading";


const styles = theme => ({
    root: {
        width: 500
    },
    json: {
        overflow: 'auto'
    }
});

function Master ({ events, currentlySending, generateConvos, generateEmptyHangouts, classes }) {
    const [values, setValues] = useState({
        convo_name: "",
        event_uid: "",
        num_hangouts: 4,
        num_threads: 4,
        hangout_name: "Hangout",
        error: false
    });

    console.log(values);

    const handleGenerate = event => {
        generateEmptyHangouts(values.hangout_name, values.num_hangouts, values.num_threads)
    };

    const handleSubmit = event => {
        if (values.event_uid.length > 0 && values.convo_name.length > 0) {
            generateConvos(values.event_uid, values.convo_name);
        } else {
            setValues({
                ...values,
                error: true
            })
        }
    };

    const handleChange = event => {
        setValues({
            ...values,
            [event.target.name]: event.target.value,
            error: false
        })
    };

    const handleNumChange = event => {
        setValues({
            ...values,
            [event.target.name]: Number(event.target.value),
            error: false
        })
    };

    console.log(values);

    function showEventDetails() {
        const selectedEvent = events.filter((event) => event.id === values.event_uid)[0];
        return (
            <ReactJson collapsed src={selectedEvent}/>
        )
    }

    return (
        <div>
            {!currentlySending ? <MainLayout>
                <Grid container spacing={4}>
                    <Grid item md={6} xs={12}>
                        <Card className={classes.root}>
                            <CardHeader title={"Generate Conversations"}/>
                            <Divider/>
                            <CardContent>
                                <FormControl
                                    error={values.error}
                                    fullWidth
                                    variant={"outlined"}
                                >
                                    <InputLabel>Event Name</InputLabel>
                                    <Select
                                        value={values.event_uid}
                                        required
                                        name={"event_uid"}
                                        onChange={handleChange}
                                    >
                                        {events.map((event) => {
                                            return <MenuItem value={event.id}>{event.displayName}</MenuItem>
                                        })}
                                    </Select>
                                </FormControl>
                                {values.event_uid ? showEventDetails() : null}
                                <TextField
                                    fullWidth
                                    error={values.error}
                                    value={values.convo_name}
                                    name={"convo_name"}
                                    label={"Conversation Name"}
                                    variant="outlined"
                                    margin="dense"
                                    onChange={handleChange}
                                />
                            </CardContent>
                            <CardActions>
                                <Button
                                    color="primary"
                                    variant="contained"
                                    onClick={handleSubmit}>
                                    Generate
                                </Button>
                            </CardActions>
                        </Card>
                    </Grid>
                    <Grid item md={6} xs={12}>
                        <Card className={classes.root}>
                            <CardHeader title={"Generate Empty Hangouts"}/>
                            <Divider/>
                            <CardContent>
                                <Grid container spacing={2}>
                                    <Grid item xs={12} md={6}>
                                        <TextField
                                            fullWidth
                                            type={"number"}
                                            error={values.error}
                                            value={values.num_hangouts}
                                            name={"num_hangouts"}
                                            label={"Number of Hangouts"}
                                            variant="outlined"
                                            margin="dense"
                                            onChange={handleNumChange}
                                        />
                                    </Grid>
                                    <Grid item xs={12} md={6}>
                                        <TextField
                                            fullWidth
                                            type={"number"}
                                            error={values.error}
                                            value={values.num_threads}
                                            name={"num_threads"}
                                            label={"Number of Threads"}
                                            variant="outlined"
                                            margin="dense"
                                            onChange={handleNumChange}
                                        />
                                    </Grid>
                                    <Grid item md={12}>
                                        <TextField
                                            fullWidth
                                            error={values.error}
                                            value={values.hangout_name}
                                            name={"hangout_name"}
                                            label={"Hangouts Name"}
                                            variant="outlined"
                                            margin="dense"
                                            onChange={handleChange}
                                        />
                                    </Grid>
                                </Grid>
                            </CardContent>
                            <CardActions>
                                <Button
                                    color="primary"
                                    variant="contained"
                                    onClick={handleGenerate}>
                                    Generate
                                </Button>
                            </CardActions>
                        </Card>
                    </Grid>
                </Grid>
            </MainLayout> : <Loading/>}
        </div>
    )
}

export default withStyles(styles)(Master);