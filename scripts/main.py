# Import modules 
import data_read
import manipulation  
import analysis 

# Higher level funcion

def get_analysis(pop_density_filepath, locations_filepath, output_filepath): 

    """Higher level function calling all functions in order from the function_script.py file"""


    pop_density = data_read.read_cleaned_data(pop_density_filepath)
    locations = data_read.read_cleaned_data(locations_filepath )

    pop_density = manipulation.access_country_code(pop_density)
    
    columns_to_drop = ["parent_code", "year"]
    pop_density = manipulation.drop_cols(pop_density, columns_to_drop)

    pop_density = manipulation.to_integer(pop_density, "country_code", "CC")
    locations = manipulation.to_integer(locations, "location_id", '"')

    pop_density_locations = manipulation.join_frames(left_dataframe=pop_density,
                                                    right_dataframe=locations,
                                                    left_column="country_code",
                                                    right_column="location_id")   
    # Added module name here
    aggreagation = analysis.aggregate_mean(dataframe=pop_density_locations,
                                            groupby_column="sdg_region_name",
                                            statistic_column="population_density")
                                    
    formatted_statistic = analysis.format_frame(aggreagation, "mean_population_density")


    formatted_statistic.to_csv(output_filepath, index=False)


get_analysis(pop_density_filepath = "mod_prog_workshop/data/population_density_2019.csv", 
             locations_filepath = ("mod_prog_workshop/data/locations.csv"),
             output_filepath = "mod_prog_workshop/outputs/mean_population_density_output.csv")