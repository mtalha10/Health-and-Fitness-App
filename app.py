import gradio as gr


def calculate_sleep_quality_and_time(total_minutes_asleep, total_time_in_bed):
    # Calculate sleep duration in hours
    sleep_duration_hours = total_minutes_asleep / 60

    # Calculate time in bed in hours
    time_in_bed_hours = total_time_in_bed / 60

    # Convert time in bed to hours and minutes
    time_in_bed_minutes = int((time_in_bed_hours % 1) * 60)  # Extract minutes
    time_in_bed_hours = int(time_in_bed_hours)  # Extract hours

    # Predict sleep quality based on sleep duration
    if sleep_duration_hours >= 7:
        sleep_quality = "Average"
    elif 5 <= sleep_duration_hours < 7:
        sleep_quality = "Good"
    else:
        sleep_quality = "Bad"

    # Output the results
    result = f"Sleep quality: {sleep_quality}\nTotal time in bed: {time_in_bed_hours} hours and {time_in_bed_minutes} minutes"
    return result


def calculate_caloric_expenditure_and_health(calories):
    # Calculate healthy calorie burn (e.g., based on BMR and activity level)
    healthy_calories_burn = 2000  # Example: Assume a healthy calorie burn goal of 2000 calories

    # Determine if calorie burn is healthy or not
    if calories >= healthy_calories_burn:
        health_status = "Healthy"
    else:
        health_status = "Unhealthy"

    # Output the results
    result = f"Calories burned: {calories}\nHealthy calorie burn goal: {healthy_calories_burn} calories\nHealth status: {health_status}"
    return result


def analyze_activity_trends(total_steps, total_distance):
    # Analyze trends in Total Steps and Total Distance
    if total_steps >= 10000:
        steps_trend = "High"
    elif 5000 <= total_steps < 10000:
        steps_trend = "Moderate"
    else:
        steps_trend = "Low"

    if total_distance >= 8:
        distance_trend = "High"
    elif 4 <= total_distance < 8:
        distance_trend = "Moderate"
    else:
        distance_trend = "Low"

    # Output the results
    result = f"Total Steps Trend: {steps_trend}\nTotal Distance Trend: {distance_trend}"
    return result


def calculate_all_functions(total_minutes_asleep, total_time_in_bed, calories, total_steps, total_distance):
    sleep_result = calculate_sleep_quality_and_time(total_minutes_asleep, total_time_in_bed)
    calorie_result = calculate_caloric_expenditure_and_health(calories)
    activity_result = analyze_activity_trends(total_steps, total_distance)

    combined_result = f"Sleep Quality and Time:\n{sleep_result}\n\nCaloric Expenditure and Health:\n{calorie_result}\n\nActivity Trends:\n{activity_result}"
    return combined_result


# Create the Gradio interface with tabs
with gr.Blocks() as demo:
    gr.Markdown("# Health and Fitness Analysis")

    with gr.Tab("All Functions"):
        with gr.Tab("All Functions"):
            with gr.Row():
                with gr.Column():
                    all_inputs = [
                        gr.Number(label="Total Minutes Asleep"),
                        gr.Number(label="Total Time in Bed (minutes)"),
                        gr.Number(label="Total Calories Burned"),
                        gr.Number(label="Total Steps"),
                        gr.Number(label="Total Distance (in miles)")
                    ]
                with gr.Column():
                    all_output = gr.Textbox(label="Combined Results")
                    all_button = gr.Button("Calculate All")
                    all_button.click(calculate_all_functions, inputs=all_inputs, outputs=all_output)

        # with gr.Row():
        #     with gr.Column():
        #         sleep_inputs_all = [
        #             gr.Number(label="Total Minutes Asleep"),
        #             gr.Number(label="Total Time in Bed (minutes)")
        #         ]
        #         sleep_output_all = gr.Textbox(label="Sleep Quality and Time")
        #         sleep_button_all = gr.Button("Calculate Sleep")
        #         sleep_button_all.click(calculate_sleep_quality_and_time, inputs=sleep_inputs_all, outputs=sleep_output_all)
        #
        #     with gr.Column():
        #         calorie_input_all = gr.Number(label="Total Calories Burned")
        #         calorie_output_all = gr.Textbox(label="Caloric Expenditure and Health")
        #         calorie_button_all = gr.Button("Calculate Calories")
        #         calorie_button_all.click(calculate_caloric_expenditure_and_health, inputs=calorie_input_all, outputs=calorie_output_all)
        #
        #     with gr.Column():
        #         activity_inputs_all = [
        #             gr.Number(label="Total Steps"),
        #             gr.Number(label="Total Distance (in miles)")
        #         ]
        #         activity_output_all = gr.Textbox(label="Activity Trends")
        #         activity_button_all = gr.Button("Analyze Activity")
        #         activity_button_all.click(analyze_activity_trends, inputs=activity_inputs_all, outputs=activity_output_all)

    with gr.Tab("Sleep Quality"):
        sleep_inputs = [
            gr.Number(label="Total Minutes Asleep"),
            gr.Number(label="Total Time in Bed (minutes)")
        ]
        sleep_output = gr.Textbox(label="Sleep Quality and Time")
        sleep_button = gr.Button("Calculate")
        sleep_button.click(calculate_sleep_quality_and_time, inputs=sleep_inputs, outputs=sleep_output)

    with gr.Tab("Caloric Expenditure"):
        calorie_input = gr.Number(label="Total Calories Burned")
        calorie_output = gr.Textbox(label="Caloric Expenditure and Health")
        calorie_button = gr.Button("Calculate")
        calorie_button.click(calculate_caloric_expenditure_and_health, inputs=calorie_input, outputs=calorie_output)

    with gr.Tab("Activity Trends"):
        activity_inputs = [
            gr.Number(label="Total Steps"),
            gr.Number(label="Total Distance (in miles)")
        ]
        activity_output = gr.Textbox(label="Activity Trends")
        activity_button = gr.Button("Analyze")
        activity_button.click(analyze_activity_trends, inputs=activity_inputs, outputs=activity_output)

demo.launch(share=True)