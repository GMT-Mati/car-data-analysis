def generate_report(results):
    """Generate a report from the results of the data analysis"""
    report = 'Number of listings by make and model:\n\n'
    for make_model_count in results['make_model_counts']:
        report += f"{make_model_count['make']} {make_model_count['model']}: {make_model_count['count']}\n"
    report += f"\nAverage age of cars: {results['avg_age']:.1f}\n\n"
    report += 'Average price of cars by make and model:\n\n'
    for avg_price in results['avg_prices']:
        report += f"{avg_price['make']} {avg_price['model']}: {avg_price['avg_price']:.2f}\n"
    return report

# This code defines the generate_report function, which takes the dictionary of results produced by
# the analyze_data function and generates a report in string format.
# The function iterates over the make_model_counts and avg_prices lists in the results dictionary to create the report.
# The report is returned as a string.
