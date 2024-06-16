# Medicaid-Drug-Rebate-Program
-------------------------------------------------------------------------------
Background
-------------------------------------------------------------------------------
Medi-Cal is California's Medicaid health care program. This program pays for various medical services for children and adults with limited income and resources. Medi-Cal is supported by Federal and state taxes. Medi-Cal is a large program comprising many programs designed to assist Californians in various family and medical situations.
<img width="476" alt="image" src="https://github.com/lleiva25/Medicaid-Drug-Rebate-Program/assets/140974405/3c68627a-ada7-4392-bdf2-d5154665a318">

-------------------------------------------------------------------------------
Powerpoint
-------------------------------------------------------------------------------
Link: https://github.com/lleiva25/Medicaid-Drug-Rebate-Program/blob/main/Medi-Cal%20Presentation.pptx

<img width="459" alt="Screenshot 2024-06-10 at 5 30 07 PM" src="https://github.com/lleiva25/Medicaid-Drug-Rebate-Program/assets/140974405/3fed7468-7a9e-4757-b522-2ee20dd1c624">

-------------------------------------------------------------------------------
Meta Data
-------------------------------------------------------------------------------
| Data Keys | Decscription |
| ------------- | ------------- |
|Utilization Type  | Constant “FFSU” or “MCOU”. |
| Labeller Code  | First segment of NDC that identifies the manufacturer, labeler, relabeler, packager, repackager or distributor of the drug.  |
| Product Code  | Second segment of NDC.  |
| Package Size Code | Third segment of NDC.  |
| Quarter  | Valid values are: 1 = January 1 – March 31, 2 = April 1 – June 30, 3 = July 1 – September 30, 4 = October 1 – December 31  |
| Product Name  | First 10 characters of product name as approved by the Food and Drug Administration (FDA) |
| Suppression Used |A checkmark in the "Suppression Used" column notes suppressed data. CMS applies counter or secondary suppression in cases where only one prescription is suppressed for primary reasons (e.g., one prescription in a state). Also, if one sub-group (e.g., number of prescriptions) is suppressed, then the other sub-groups are suppressed. |
| Units Reimbursed  | FFS Units - The number of units (based on Unit Type) of the drug 11-digit NDC reimbursed by the state during the quarter/year covered. MCO Units - The number of units (based on Unit Type) of the 11-digit NDC dispensed during the quarter/year covered. |
|Number of Prescriptions | The number of prescriptions should include any prescription for which Medicaid paid a portion of the claim, as well as those prescriptions for which Medicaid paid the claim in full.  |
|Total Amount Reimbursed  |The FFS or MCO total amount reimbursed by both Medicaid and non-Medicaid entities to pharmacies or other providers for the 11-digit NDC drug in the period covered. |
|Medicaid Amount Reimbursed  | The amount reimbursed by the Medicaid Program ONLY to pharmacies or other providers for the 11-digit NDC FFS or MCO drug in the quarter/year covered. |
| Non-Medicaid Amount Reimbursed  | The amount reimbursed by non-Medicaid entities to pharmacies or other providers for the 11-digit NDC FFS or MCO drug in thequarter/year covered.  |
| Latitude  | The angular distance of a place north or south of the earth's equator, or of a celestial object north or south of the celestial equator, usually expressed in degrees and minutes.  |
| Longitude  | The angular distance of a place east or west of the meridian at Greenwich, England, or west of the standard meridian of a celestial object, usually expressed in degrees and minutes. |
| Location  | Location within state. Derived from state code provides ability to create maps and geographic comparisons.  |

-------------------------------------------------------------------------------
Dashboard 
-------------------------------------------------------------------------------
Link to Dashboard: https://medicaid-drug-rebate-program.onrender.com/

![Reimbursement_Type_Pie](https://github.com/lleiva25/Medicaid-Drug-Rebate-Program/assets/140974405/0ea50f4c-c170-4700-9953-13b2fb8c04d8)

![No_Prescription_Scatterplot](https://github.com/lleiva25/Medicaid-Drug-Rebate-Program/assets/140974405/fadb5f11-9c4e-4a87-ba2d-0e95810944eb)

![Top10_Reimbursed_Products_Bar](https://github.com/lleiva25/Medicaid-Drug-Rebate-Program/assets/140974405/58c56c1a-3fbd-439a-93d3-209a0579c9d3)

-------------------------------------------------------------------------------
Process
-------------------------------------------------------------------------------
1. Import dependencies.
2. Extract database.
3. Remove unneeded columns: 'state','year','ndc','labeler_code', & 'product_code'.
4. Remove additional spaces after product name.
5. Iterate a variety of loops to generate datasets based on quarter.
6. Clean up the groupby dataframe and save to output folder as json or csv.
-------------------------------------------------------------------------------
References
-------------------------------------------------------------------------------

CA Benefits [https://www.benefits.gov/benefit/1620]
Data Medicaid [https://data.medicaid.gov/dataset/d890d3a9-6b00-43fd-8b31-fcba4c8e2909/data?conditions%5b0%5d%5bresource%5d=t&conditions%5b0%5d%5bproperty%5d=state&conditions%5b0%5d%5bvalue%5d=CA&conditions%5b0%5d%5boperator%5d=%3D]
