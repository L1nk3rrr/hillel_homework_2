# hillel_homework_2
Flask app homework

## Endpoints

1. `/requrements`
   - Description: Get requirements data.
   
2. `/requrements_beauty`
   - Description: Get requirements data with a formatted view.

3. `/generate-users/`
   - Description: Generate fake users.
   - Query Parameter: `qty` (optional, 100 by default) - Number of users to generate.

4. `/mean/`
   - Description: Calculate average measurements from a CSV file.
   - Query Parameter: `rounding` (optional, 2 by default) - Rounding factor for average values.

5. `/space/`
   - Description: Get the number of astronauts in space.
