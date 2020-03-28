import React, { useState, useEffect } from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import { withStyles, useTheme } from '@material-ui/core/styles';
import {
    Card,
    MenuItem,
    Chip,
    Input,
    CardHeader,
    CardContent,
    CardActions,
    Divider,
    Grid,
    Button,
    TextField
} from '@material-ui/core';
import Select from '@material-ui/core/Select';
import FormTextField from "../form/FormTextField";
import InputLabel from "@material-ui/core/InputLabel";
import FormControl from "@material-ui/core/FormControl";

const styles = theme => ({
  chips: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  chip: {
    margin: 2,
  }
});

const all_interests = [
    'cooking',
    'coding',
    'hiking'
]

// const all_interests = [
//   {
//     value: 'cooking',
//     label: 'Cooking'
//   },
//   {
//     value: 'coding',
//     label: 'Coding'
//   },
//   {
//     value: 'hiking',
//     label: 'Hiking'
//   }
// ];

function getStyles(interest, interests, theme) {
  return {
    fontWeight:
      interests.indexOf(interest) === -1
        ? theme.typography.fontWeightRegular
          : theme.typography.fontWeightMedium
  }
}

function AccountDetails({ profile, setProfile, className, classes, ...rest }) {
  const theme = useTheme();

  const [values, setValues] = useState({
    displayName: '',
    state: '',
    country: '',
    interests: []
  });

  useEffect(() => {
    setValues(profile)
  }, [profile]);

  console.log(values);

  const handleChange = event => {
    setValues({
      ...values,
      [event.target.name]: event.target.value
    })
  }

  const handleSubmit = event => {
    event.preventDefault();
    setProfile(values);
  };

  const states = [
    {
      value: 'Georgia',
      label: 'Georgia'
    },
    {
      value: 'Alabama',
      label: 'Alabama'
    },
    {
      value: 'New York',
      label: 'New York'
    },
    {
      value: 'San Francisco',
      label: 'San Francisco'
    }
  ];

  return (
    <Card
      {...rest}
      className={clsx(classes.root, className)}
    >
      <form
        autoComplete="off"
        onSubmit={handleSubmit}
        noValidate
      >
        <CardHeader
          subheader="The information can be edited"
          title="Profile"
        />
        <Divider />
        <CardContent>
          <Grid
            container
            spacing={3}
          >
            <Grid
              item
              md={12}
              xs={12}
            >
              <TextField
                fullWidth
                helperText="Please specify the full name"
                label="Full name"
                margin="dense"
                name="displayName"
                required
                value={values.displayName}
                variant="outlined"
                onChange={handleChange}
              />
            </Grid>
            {/*<Grid*/}
            {/*  item*/}
            {/*  md={6}*/}
            {/*  xs={12}*/}
            {/*>*/}
            {/*  <TextField*/}
            {/*    fullWidth*/}
            {/*    label="Last name"*/}
            {/*    margin="dense"*/}
            {/*    name="lastName"*/}
            {/*    onChange={handleChange}*/}
            {/*    required*/}
            {/*    value={values.lastName}*/}
            {/*    variant="outlined"*/}
            {/*  />*/}
            {/*</Grid>*/}
            {/*<Grid*/}
            {/*  item*/}
            {/*  md={6}*/}
            {/*  xs={12}*/}
            {/*>*/}
            {/*  <TextField*/}
            {/*    fullWidth*/}
            {/*    label="Email Address"*/}
            {/*    margin="dense"*/}
            {/*    name="email"*/}
            {/*    onChange={handleChange}*/}
            {/*    required*/}
            {/*    value={values.email}*/}
            {/*    variant="outlined"*/}
            {/*  />*/}
            {/*</Grid>*/}
            {/*<Grid*/}
            {/*  item*/}
            {/*  md={6}*/}
            {/*  xs={12}*/}
            {/*>*/}
            {/*  <TextField*/}
            {/*    fullWidth*/}
            {/*    label="Phone Number"*/}
            {/*    margin="dense"*/}
            {/*    name="phone"*/}
            {/*    onChange={handleChange}*/}
            {/*    type="number"*/}
            {/*    value={values.phone}*/}
            {/*    variant="outlined"*/}
            {/*  />*/}
            {/*</Grid>*/}
            <Grid
              item
              md={6}
              xs={12}
            >
              <TextField
                fullWidth
                label="Select State"
                margin="dense"
                name="state"
                required
                select
                // eslint-disable-next-line react/jsx-sort-props
                SelectProps={{ native: true }}
                value={values.state}
                variant="outlined"
                onChange={handleChange}
              >
                {states.map(option => (
                  <option
                    key={option.value}
                    value={option.value}
                  >
                    {option.label}
                  </option>
                ))}
              </TextField>
            </Grid>
            <Grid
              item
              md={6}
              xs={12}
            >
              <TextField
                fullWidth
                label="Country"
                margin="dense"
                name="country"
                required
                value={values.country}
                variant="outlined"
                onChange={handleChange}
              />
            </Grid>
          </Grid>
        </CardContent>
        <Divider />
        <CardContent>
          <Grid
            container
            spacing={3}
          >
            <Grid
                item
                md={12}
                xs={12}
            >
              <FormControl
                  fullWidth
              >
                <InputLabel>Interests</InputLabel>
                <Select
                    multiple
                    name='interests'
                    value={values.interests}
                    onChange={handleChange}
                    input={<Input id='select-multiple-chip'/>}
                    renderValue={selected => (
                        <div className={classes.chips}>
                          {selected.map(interest => (
                              <Chip key={interest} label={interest} className={classes.chip} />
                          ))}
                        </div>
                    )}
                >
                  {all_interests.map(interest => (
                      <MenuItem key={interest} value={interest} style={getStyles(interest, values.interests, theme)}>
                        {interest}
                      </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>
          </Grid>
        </CardContent>
        <Divider />
        <CardActions>
          <Button
            color="primary"
            variant="contained"
            type="submit"
          >
            Save details
          </Button>
        </CardActions>
      </form>
    </Card>
  );
};

AccountDetails.propTypes = {
  className: PropTypes.string
};

export default withStyles(styles)(AccountDetails);