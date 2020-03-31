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
import {CountryRegionData, CountryDropdown, RegionDropdown} from "react-country-region-selector";
import {Autocomplete} from "@material-ui/lab";

const styles = theme => ({
  chips: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  chip: {
    margin: 2,
  }
});

// const all_interests = [
//     'cooking',
//     'coding',
//     'hiking'
// ]

// const all_majors = [
//     'Computer Science',
//     'Neuroscience',
//     'Psychology'
// ]

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

function getStyles(major, majors, theme) {
  return {
    fontWeight:
      majors.indexOf(major) === -1
        ? theme.typography.fontWeightRegular
          : theme.typography.fontWeightMedium
  }
}

function AccountDetails({ title,
                          subtitle,
                          profile,
                          allMajors,
                          setProfile,
                          className,
                          classes, ...rest }) {
  const theme = useTheme();

  const [values, setValues] = useState({
    displayName: '',
    state: '',
    country: '',
    majors: []
  });

  useEffect(() => {
    setValues(profile)
  }, [profile]);

  console.log(values);
  console.log(allMajors);

  const handleChange = event => {
    setValues({
      ...values,
      [event.target.name]: event.target.value
    })
  }

  const selectMajors = (event, value) => {
      setValues({
          ...values,
          majors: value
      })
  }

  const selectCountry = event => {
    setValues({
      ...values,
      state: "",
      country: event.target.value
    })
  }

  const getRegions = country => {
    if (!country) {
      return [];
    }
    const country_data = CountryRegionData.filter(entry => entry[0] === country)[0];
    return country_data[2].split("|").map(regionPair => {
      let [regionName, regionShortCode = null] = regionPair.split("~");
      return regionName;
    });
  };

  const handleSubmit = event => {
    event.preventDefault();
    setProfile(values);
  };

  // const states = [
  //   {
  //     value: 'Georgia',
  //     label: 'Georgia'
  //   },
  //   {
  //     value: 'Alabama',
  //     label: 'Alabama'
  //   },
  //   {
  //     value: 'New York',
  //     label: 'New York'
  //   },
  //   {
  //     value: 'San Francisco',
  //     label: 'San Francisco'
  //   }
  // ];

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
          subheader={subtitle}
          title={title}
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
            <Grid item md={6} xs={12}>
              <TextField
                  fullWidth
                  value={values.country}
                  name={"country"}
                  label="Country"
                  select
                  variant="outlined"
                  margin="dense"
                  onChange={selectCountry}
              >
                {CountryRegionData.map((option, index) => {
                  return <MenuItem key={option[0]} value={option[0]}>{option[0]}</MenuItem>
                })}
              </TextField>
            </Grid>
            <Grid item md={6} xs={12}>
              <TextField
                  fullWidth
                  value={values.state}
                  name={"state"}
                  label="State/Region"
                  select
                  variant="outlined"
                  margin="dense"
                  onChange={handleChange}
              >
                {getRegions(values.country).map(
                    (option, index) => {
                      return <MenuItem key={option} value={option}>
                        {option}
                      </MenuItem>
                    }
                )}
              </TextField>
            </Grid>
            {/*<Grid item md={6} xs={12}>*/}
            {/*  <CountryDropdown*/}
            {/*      value={values.country}*/}
            {/*      onChange={(val) => selectCountry(val)}*/}
            {/*  />*/}
            {/*</Grid>*/}
            {/*<Grid item md={6} xs={12}>*/}
            {/*  <RegionDropdown*/}
            {/*      country={values.country}*/}
            {/*      value={values.state}*/}
            {/*      onChange={(val) => selectState(val)}*/}
            {/*  />*/}
            {/*</Grid>*/}
            {/*<Grid*/}
            {/*  item*/}
            {/*  md={6}*/}
            {/*  xs={12}*/}
            {/*>*/}
            {/*  <TextField*/}
            {/*    fullWidth*/}
            {/*    label="Select State"*/}
            {/*    margin="dense"*/}
            {/*    name="state"*/}
            {/*    required*/}
            {/*    select*/}
            {/*    // eslint-disable-next-line react/jsx-sort-props*/}
            {/*    SelectProps={{ native: true }}*/}
            {/*    value={values.state}*/}
            {/*    variant="outlined"*/}
            {/*    onChange={handleChange}*/}
            {/*  >*/}
            {/*    {states.map(option => (*/}
            {/*      <option*/}
            {/*        key={option.value}*/}
            {/*        value={option.value}*/}
            {/*      >*/}
            {/*        {option.label}*/}
            {/*      </option>*/}
            {/*    ))}*/}
            {/*  </TextField>*/}
            {/*</Grid>*/}
            {/*<Grid*/}
            {/*  item*/}
            {/*  md={6}*/}
            {/*  xs={12}*/}
            {/*>*/}
            {/*  <TextField*/}
            {/*    fullWidth*/}
            {/*    label="Country"*/}
            {/*    margin="dense"*/}
            {/*    name="country"*/}
            {/*    required*/}
            {/*    value={values.country}*/}
            {/*    variant="outlined"*/}
            {/*    onChange={handleChange}*/}
            {/*  />*/}
            {/*</Grid>*/}
          </Grid>
        </CardContent>
        <Divider />
        <CardContent>
          <Grid
            container
            spacing={3}
          >
            <Grid item md={12} xs={12}>
              <Autocomplete
                  multiple
                  getOptionLabel={(option) => option}
                  options={allMajors}
                  value={values.majors}
                  renderInput={(params)=> (
                      <TextField {...params} variant={"outlined"} label={"(Intended) Majors"}/>
                  )}
                  onChange={selectMajors}
              />
            </Grid>
            {/*<Grid*/}
            {/*    item*/}
            {/*    md={12}*/}
            {/*    xs={12}*/}
            {/*>*/}
            {/*  <FormControl*/}
            {/*      fullWidth*/}
            {/*  >*/}
            {/*    <InputLabel>Majors</InputLabel>*/}
            {/*    <Select*/}
            {/*        multiple*/}
            {/*        name="majors"*/}
            {/*        value={values.majors}*/}
            {/*        onChange={handleChange}*/}
            {/*        input={<Input id='select-multiple-chip'/>}*/}
            {/*        renderValue={selected => (*/}
            {/*            <div className={classes.chips}>*/}
            {/*              {selected.map(major => (*/}
            {/*                  <Chip key={major} label={major} className={classes.chip} />*/}
            {/*              ))}*/}
            {/*            </div>*/}
            {/*        )}*/}
            {/*    >*/}
            {/*      {all_majors.map(major => (*/}
            {/*          <MenuItem key={major} value={major} style={getStyles(major, values.majors, theme)}>*/}
            {/*            {major}*/}
            {/*          </MenuItem>*/}
            {/*      ))}*/}
            {/*    </Select>*/}
            {/*  </FormControl>*/}
            {/*</Grid>*/}
          </Grid>
        </CardContent>
        <Divider />
        <CardActions>
          <Button
            color="primary"
            variant="contained"
            type="submit"
          >
            Save
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