def findDecision(obj): #float(obj[0]): age, obj[1]: workclass, float(obj[2]): fnlwgt, obj[3]: education, obj[4]: education-num, obj[5]: marital-status, obj[6]: occupation, obj[7]: relationship, obj[8]: race, obj[9]: sex, float(obj[10]): capital-gain, float(obj[11]): capital-loss, float(obj[12]): hours-per-week, obj[13]: native-country
	# {"feature": "capital-gain", "instances": 32561, "metric_value": 0.7964, "depth": 1}
	if float(obj[10])<=8462.827520655317:
		# {"feature": "education-num", "instances": 31710, "metric_value": 0.7618, "depth": 2}
		if obj[4]<=14:
			# {"feature": "marital-status", "instances": 30891, "metric_value": 0.7389, "depth": 3}
			if obj[5] == 'Married-civ-spouse':
				# {"feature": "age", "instances": 13852, "metric_value": 0.9769, "depth": 4}
				if float(obj[0])>18.88526350825298:
					# {"feature": "fnlwgt", "instances": 13843, "metric_value": 0.977, "depth": 5}
					if float(obj[2])>13769:
						# {"feature": "capital-loss", "instances": 13842, "metric_value": 0.9771, "depth": 6}
						if float(obj[11])<=1508.4669661576388:
							# {"feature": "education", "instances": 13036, "metric_value": 0.9669, "depth": 7}
							if obj[3] == 'HS-grad':
								# {"feature": "hours-per-week", "instances": 4554, "metric_value": 0.8697, "depth": 8}
								if float(obj[12])>19.493059349631555:
									# {"feature": "native-country", "instances": 4418, "metric_value": 0.8784, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "workclass", "instances": 4146, "metric_value": 0.8851, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "race", "instances": 3044, "metric_value": 0.8759, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 2766, "metric_value": 0.8926, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "relationship", "instances": 767, "metric_value": 0.8905, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 755, "metric_value": 0.89, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "relationship", "instances": 383, "metric_value": 0.8245, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 354, "metric_value": 0.8266, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 26, "metric_value": 0.8404, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Transport-moving':
													# {"feature": "relationship", "instances": 319, "metric_value": 0.9075, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 310, "metric_value": 0.9106, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													# {"feature": "relationship", "instances": 279, "metric_value": 0.9253, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 243, "metric_value": 0.9375, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 31, "metric_value": 0.7706, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														elif obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "sex", "instances": 210, "metric_value": 0.9968, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "relationship", "instances": 179, "metric_value": 0.9962, "depth": 14}
														if obj[7] == 'Husband':
															return '>50K'
														elif obj[7] == 'Other-relative':
															return '>50K'
														else: return '>50K'
													elif obj[9] == 'Female':
														# {"feature": "relationship", "instances": 31, "metric_value": 0.9992, "depth": 14}
														if obj[7] == 'Wife':
															return '>50K'
														elif obj[7] == 'Other-relative':
															return '<=50K'
														else: return '<=50K'
													else: return '>50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "relationship", "instances": 204, "metric_value": 0.9526, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 104, "metric_value": 0.8905, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 92, "metric_value": 0.9986, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "relationship", "instances": 203, "metric_value": 0.8357, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 171, "metric_value": 0.8564, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 25, "metric_value": 0.795, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Not-in-family':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													# {"feature": "relationship", "instances": 142, "metric_value": 0.7163, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 137, "metric_value": 0.7161, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													# {"feature": "relationship", "instances": 121, "metric_value": 0.5635, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 93, "metric_value": 0.4924, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 24, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Farming-fishing':
													# {"feature": "relationship", "instances": 60, "metric_value": 0.5197, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 58, "metric_value": 0.5313, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Tech-support':
													# {"feature": "relationship", "instances": 45, "metric_value": 0.9996, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 38, "metric_value": 0.998, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Other-relative':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '>50K'
												elif obj[6] == 'Protective-serv':
													# {"feature": "relationship", "instances": 28, "metric_value": 0.8631, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 27, "metric_value": 0.8767, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Priv-house-serv':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "relationship", "instances": 215, "metric_value": 0.6518, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "occupation", "instances": 170, "metric_value": 0.7219, "depth": 13}
													if obj[6] == 'Machine-op-inspct':
														# {"feature": "sex", "instances": 38, "metric_value": 0.7897, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 32, "metric_value": 0.7579, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Transport-moving':
														# {"feature": "sex", "instances": 25, "metric_value": 0.5294, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Handlers-cleaners':
														# {"feature": "sex", "instances": 24, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Other-service':
														# {"feature": "sex", "instances": 17, "metric_value": 0.7871, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Adm-clerical':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Sales':
														# {"feature": "sex", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Farming-fishing':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Tech-support':
														return '>50K'
													elif obj[6] == 'Protective-serv':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													# {"feature": "occupation", "instances": 39, "metric_value": 0.2918, "depth": 13}
													if obj[6] == 'Other-service':
														# {"feature": "sex", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Adm-clerical':
														return '<=50K'
													elif obj[6] == 'Machine-op-inspct':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Handlers-cleaners':
														return '<=50K'
													elif obj[6] == 'Craft-repair':
														return '<=50K'
													elif obj[6] == 'Tech-support':
														return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '<=50K'
													elif obj[6] == 'Priv-house-serv':
														return '<=50K'
													elif obj[6] == 'Sales':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												elif obj[7] == 'Not-in-family':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												# {"feature": "occupation", "instances": 30, "metric_value": 0.5665, "depth": 12}
												if obj[6] == 'Transport-moving':
													# {"feature": "relationship", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														return '>50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												# {"feature": "occupation", "instances": 19, "metric_value": 0.7425, "depth": 12}
												if obj[6] == 'Transport-moving':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Other':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "relationship", "instances": 481, "metric_value": 0.7684, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 456, "metric_value": 0.7548, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "occupation", "instances": 438, "metric_value": 0.7587, "depth": 13}
													if obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 127, "metric_value": 0.7464, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Farming-fishing':
														# {"feature": "sex", "instances": 115, "metric_value": 0.6858, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														# {"feature": "sex", "instances": 63, "metric_value": 0.7642, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Sales':
														# {"feature": "sex", "instances": 60, "metric_value": 0.8366, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Transport-moving':
														# {"feature": "sex", "instances": 41, "metric_value": 0.839, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Other-service':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Machine-op-inspct':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Tech-support':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Handlers-cleaners':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '<=50K'
													elif obj[6] == 'Adm-clerical':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "occupation", "instances": 11, "metric_value": 0.8454, "depth": 13}
													if obj[6] == 'Sales':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Other-service':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Craft-repair':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Wife':
												# {"feature": "occupation", "instances": 24, "metric_value": 0.9183, "depth": 12}
												if obj[6] == 'Sales':
													# {"feature": "race", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Own-child':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Local-gov':
											# {"feature": "occupation", "instances": 226, "metric_value": 0.8979, "depth": 11}
											if obj[6] == 'Protective-serv':
												# {"feature": "relationship", "instances": 49, "metric_value": 0.9997, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 48, "metric_value": 0.9987, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 45, "metric_value": 0.9996, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "race", "instances": 45, "metric_value": 0.8945, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 43, "metric_value": 0.8841, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 43, "metric_value": 0.8841, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "relationship", "instances": 41, "metric_value": 0.7121, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 39, "metric_value": 0.679, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 30, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												# {"feature": "race", "instances": 30, "metric_value": 0.469, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 22, "metric_value": 0.4395, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "relationship", "instances": 18, "metric_value": 0.5033, "depth": 14}
														if obj[7] == 'Husband':
															return '<=50K'
														elif obj[7] == 'Other-relative':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Other':
													return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "race", "instances": 26, "metric_value": 0.9957, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 23, "metric_value": 0.9877, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 20, "metric_value": 0.9928, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "sex", "instances": 16, "metric_value": 0.9887, "depth": 12}
												if obj[9] == 'Female':
													# {"feature": "relationship", "instances": 12, "metric_value": 0.9799, "depth": 13}
													if obj[7] == 'Wife':
														# {"feature": "race", "instances": 11, "metric_value": 0.9457, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Male':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											# {"feature": "race", "instances": 159, "metric_value": 0.9993, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 154, "metric_value": 0.9989, "depth": 12}
												if obj[6] == 'Exec-managerial':
													# {"feature": "relationship", "instances": 62, "metric_value": 0.9932, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 61, "metric_value": 0.9951, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Sales':
													# {"feature": "relationship", "instances": 33, "metric_value": 0.994, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 31, "metric_value": 0.9812, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													# {"feature": "relationship", "instances": 30, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 30, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Farming-fishing':
													# {"feature": "relationship", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "relationship", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Other-service':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Transport-moving':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Protective-serv':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6] == 'Prof-specialty':
													return '>50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'State-gov':
											# {"feature": "occupation", "instances": 121, "metric_value": 0.8882, "depth": 11}
											if obj[6] == 'Protective-serv':
												# {"feature": "race", "instances": 33, "metric_value": 0.799, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 29, "metric_value": 0.6632, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 28, "metric_value": 0.6769, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "race", "instances": 21, "metric_value": 0.9587, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 19, "metric_value": 0.9495, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 19, "metric_value": 0.9495, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "race", "instances": 16, "metric_value": 0.6962, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 13, "metric_value": 0.6194, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														return '>50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												# {"feature": "race", "instances": 12, "metric_value": 0.8113, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Wife':
														return '<=50K'
													elif obj[7] == 'Husband':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "race", "instances": 9, "metric_value": 0.9911, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "relationship", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Tech-support':
												# {"feature": "relationship", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Farming-fishing':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Federal-gov':
											# {"feature": "race", "instances": 110, "metric_value": 0.9806, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "relationship", "instances": 87, "metric_value": 0.9576, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "occupation", "instances": 77, "metric_value": 0.9793, "depth": 13}
													if obj[6] == 'Adm-clerical':
														# {"feature": "sex", "instances": 37, "metric_value": 0.974, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 13, "metric_value": 0.9612, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Tech-support':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Transport-moving':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Machine-op-inspct':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '>50K'
													elif obj[6] == 'Farming-fishing':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													# {"feature": "occupation", "instances": 10, "metric_value": 0.469, "depth": 13}
													if obj[6] == 'Adm-clerical':
														# {"feature": "sex", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Sales':
														return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												# {"feature": "relationship", "instances": 17, "metric_value": 0.9774, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "occupation", "instances": 16, "metric_value": 0.9544, "depth": 13}
													if obj[6] == 'Adm-clerical':
														# {"feature": "sex", "instances": 12, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Transport-moving':
														return '>50K'
													elif obj[6] == 'Craft-repair':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											elif obj[8] == 'Other':
												return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Without-pay':
											return '<=50K'
										elif obj[1] == 'Never-worked':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Mexico':
										# {"feature": "race", "instances": 57, "metric_value": 0.5374, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "occupation", "instances": 51, "metric_value": 0.577, "depth": 11}
											if obj[6] == 'Other-service':
												# {"feature": "relationship", "instances": 13, "metric_value": 0.6194, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "workclass", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "workclass", "instances": 11, "metric_value": 0.684, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 9, "metric_value": 0.7642, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 9, "metric_value": 0.7642, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Husband':
													return '<=50K'
												elif obj[7] == 'Wife':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Wife':
													return '<=50K'
												elif obj[7] == 'Husband':
													return '<=50K'
												elif obj[7] == 'Own-child':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'Other':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Philippines':
										# {"feature": "race", "instances": 14, "metric_value": 0.5917, "depth": 10}
										if obj[8] == 'Asian-Pac-Islander':
											# {"feature": "occupation", "instances": 13, "metric_value": 0.3912, "depth": 11}
											if obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Tech-support':
												return '>50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Priv-house-serv':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'White':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Cuba':
										# {"feature": "occupation", "instances": 14, "metric_value": 0.9403, "depth": 10}
										if obj[6] == 'Sales':
											# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '>50K'
										elif obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Local-gov':
												return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Germany':
										# {"feature": "relationship", "instances": 14, "metric_value": 0.9403, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "race", "instances": 13, "metric_value": 0.8905, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 11, "metric_value": 0.8454, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "occupation", "instances": 9, "metric_value": 0.7642, "depth": 13}
													if obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Other-service':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												elif obj[1] == 'Self-emp-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											elif obj[8] == 'Black':
												return '>50K'
											else: return '>50K'
										elif obj[7] == 'Wife':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Italy':
										# {"feature": "workclass", "instances": 13, "metric_value": 0.9957, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "occupation", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[6] == 'Machine-op-inspct':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Transport-moving':
													return '>50K'
												elif obj[6] == 'Prof-specialty':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[7] == 'Husband':
												return '<=50K'
											elif obj[7] == 'Wife':
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'China':
										# {"feature": "occupation", "instances": 11, "metric_value": 0.4395, "depth": 10}
										if obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '>50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'South':
										# {"feature": "occupation", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Sales':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Private':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'England':
										# {"feature": "relationship", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "race", "instances": 8, "metric_value": 1.0, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Sales':
													return '>50K'
												elif obj[6] == 'Adm-clerical':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Wife':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Canada':
										# {"feature": "occupation", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Exec-managerial':
											return '>50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										elif obj[6] == 'Sales':
											return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '>50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Poland':
										# {"feature": "occupation", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '>50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Greece':
										return '<=50K'
									elif obj[13] == 'El-Salvador':
										# {"feature": "workclass", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Local-gov':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Puerto-Rico':
										return '<=50K'
									elif obj[13] == 'Jamaica':
										# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Local-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Dominican-Republic':
										# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Columbia':
										return '<=50K'
									elif obj[13] == 'Vietnam':
										# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Ireland':
										# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'Machine-op-inspct':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Ecuador':
										# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Guatemala':
										return '<=50K'
									elif obj[13] == 'Cambodia':
										# {"feature": "occupation", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Farming-fishing':
											return '>50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Laos':
										return '<=50K'
									elif obj[13] == 'Japan':
										# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6] == 'Other-service':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Nicaragua':
										return '<=50K'
									elif obj[13] == 'Peru':
										return '<=50K'
									elif obj[13] == 'Hungary':
										# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Haiti':
										return '<=50K'
									elif obj[13] == 'Portugal':
										# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[7] == 'Husband':
											return '<=50K'
										elif obj[7] == 'Wife':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'India':
										return '<=50K'
									elif obj[13] == 'Scotland':
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Trinadad&Tobago':
										return '<=50K'
									elif obj[13] == 'Iran':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Private':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Taiwan':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Self-emp-inc':
											return '>50K'
										elif obj[1] == 'Private':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Thailand':
										return '<=50K'
									elif obj[13] == 'Outlying-US(Guam-USVI-etc)':
										return '<=50K'
									elif obj[13] == 'Yugoslavia':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'Other-service':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'France':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Federal-gov':
											return '>50K'
										elif obj[1] == 'Private':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Hong':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[12])<=19.493059349631555:
									# {"feature": "sex", "instances": 136, "metric_value": 0.3515, "depth": 9}
									if obj[9] == 'Male':
										# {"feature": "workclass", "instances": 96, "metric_value": 0.1461, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 72, "metric_value": 0.1056, "depth": 11}
											if obj[6] == 'Prof-specialty':
												# {"feature": "race", "instances": 36, "metric_value": 0.1831, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 30, "metric_value": 0.2108, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "native-country", "instances": 29, "metric_value": 0.2164, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														elif obj[13] == 'Canada':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												elif obj[8] == 'Other':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "occupation", "instances": 14, "metric_value": 0.3712, "depth": 11}
											if obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Local-gov':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										elif obj[1] == 'Federal-gov':
											return '<=50K'
										elif obj[1] == 'Without-pay':
											return '<=50K'
										else: return '<=50K'
									elif obj[9] == 'Female':
										# {"feature": "native-country", "instances": 40, "metric_value": 0.669, "depth": 10}
										if obj[13] == 'United-States':
											# {"feature": "occupation", "instances": 36, "metric_value": 0.65, "depth": 11}
											if obj[6] == 'Other-service':
												# {"feature": "workclass", "instances": 12, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[7] == 'Wife':
														# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "relationship", "instances": 11, "metric_value": 0.684, "depth": 12}
												if obj[7] == 'Wife':
													# {"feature": "workclass", "instances": 10, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 10, "metric_value": 0.7219, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												return '>50K'
											elif obj[6] == 'Handlers-cleaners':
												return '>50K'
											else: return '>50K'
										elif obj[13] == 'Honduras':
											return '<=50K'
										elif obj[13] == 'Philippines':
											return '<=50K'
										elif obj[13] == 'Taiwan':
											return '<=50K'
										elif obj[13] == 'China':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Some-college':
								# {"feature": "hours-per-week", "instances": 2603, "metric_value": 0.9773, "depth": 8}
								if float(obj[12])>1:
									# {"feature": "native-country", "instances": 2602, "metric_value": 0.9773, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "occupation", "instances": 2453, "metric_value": 0.9784, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "relationship", "instances": 470, "metric_value": 0.9684, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 466, "metric_value": 0.9704, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 434, "metric_value": 0.9644, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 326, "metric_value": 0.983, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 57, "metric_value": 0.8043, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 18, "metric_value": 0.9641, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 14, "metric_value": 0.9403, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 12, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "workclass", "instances": 17, "metric_value": 0.9975, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 14, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													# {"feature": "workclass", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													# {"feature": "workclass", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													elif obj[1] == 'Self-emp-inc':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Other':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "race", "instances": 397, "metric_value": 0.9956, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 366, "metric_value": 0.9922, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 220, "metric_value": 0.9914, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 187, "metric_value": 0.9925, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 28, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Own-child':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Other-relative':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "relationship", "instances": 54, "metric_value": 0.8767, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 52, "metric_value": 0.8404, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 47, "metric_value": 0.9441, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 43, "metric_value": 0.9523, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 20, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 19, "metric_value": 0.998, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "relationship", "instances": 13, "metric_value": 0.8905, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 10, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "relationship", "instances": 12, "metric_value": 0.4138, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 12, "metric_value": 0.4138, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												# {"feature": "workclass", "instances": 20, "metric_value": 0.9928, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 10, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "relationship", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'State-gov':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Asian-Pac-Islander':
												# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[7] == 'Husband':
													return '<=50K'
												elif obj[7] == 'Wife':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											elif obj[8] == 'Other':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											# {"feature": "race", "instances": 348, "metric_value": 0.9939, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 325, "metric_value": 0.995, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 242, "metric_value": 0.9976, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 220, "metric_value": 0.999, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 19, "metric_value": 0.9819, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "relationship", "instances": 42, "metric_value": 0.9587, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 41, "metric_value": 0.9474, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 40, "metric_value": 0.7692, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 37, "metric_value": 0.6998, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "workclass", "instances": 14, "metric_value": 0.9852, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 12, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 10, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '>50K'
											elif obj[8] == 'Other':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Prof-specialty':
											# {"feature": "race", "instances": 254, "metric_value": 0.982, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 230, "metric_value": 0.9842, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 193, "metric_value": 0.9813, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 155, "metric_value": 0.9841, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 36, "metric_value": 0.9799, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 11, "metric_value": 0.9457, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "relationship", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "relationship", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[7] == 'Husband':
														return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "workclass", "instances": 13, "metric_value": 0.9612, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Wife':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Husband':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												# {"feature": "workclass", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Wife':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Other':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "workclass", "instances": 219, "metric_value": 0.9956, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 148, "metric_value": 0.9935, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 128, "metric_value": 0.9887, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 77, "metric_value": 0.9457, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 47, "metric_value": 0.9918, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Other-relative':
														return '>50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 16, "metric_value": 0.9544, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Own-child':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "relationship", "instances": 34, "metric_value": 0.9774, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 27, "metric_value": 0.951, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 20, "metric_value": 0.9341, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Other-relative':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														return '>50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												# {"feature": "race", "instances": 16, "metric_value": 0.8113, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 11, "metric_value": 0.8454, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "relationship", "instances": 12, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Wife':
													# {"feature": "race", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Husband':
													# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '<=50K'
													else: return '<=50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[7] == 'Wife':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Husband':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											elif obj[1] == 'Without-pay':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "workclass", "instances": 158, "metric_value": 0.9484, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 122, "metric_value": 0.967, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 110, "metric_value": 0.976, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 110, "metric_value": 0.976, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 10, "metric_value": 0.8813, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 11, "metric_value": 0.684, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[8] == 'White':
													return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											else: return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											# {"feature": "workclass", "instances": 123, "metric_value": 0.8722, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 109, "metric_value": 0.8357, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 106, "metric_value": 0.8187, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 93, "metric_value": 0.807, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '>50K'
													elif obj[8] == 'Other':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'State-gov':
												# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											# {"feature": "race", "instances": 113, "metric_value": 0.6109, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "relationship", "instances": 97, "metric_value": 0.6213, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "workclass", "instances": 68, "metric_value": 0.6385, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 41, "metric_value": 0.6594, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 10, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 9, "metric_value": 0.7642, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													# {"feature": "workclass", "instances": 27, "metric_value": 0.5033, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 17, "metric_value": 0.5226, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Own-child':
													return '>50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												# {"feature": "workclass", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														return '>50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "relationship", "instances": 107, "metric_value": 0.9984, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 106, "metric_value": 0.999, "depth": 12}
												if obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 59, "metric_value": 0.9831, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 55, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '<=50K'
													elif obj[8] == 'Other':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Private':
													# {"feature": "race", "instances": 21, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 13, "metric_value": 0.7793, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Other':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													# {"feature": "race", "instances": 19, "metric_value": 0.8997, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 17, "metric_value": 0.874, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "race", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Tech-support':
											# {"feature": "workclass", "instances": 102, "metric_value": 0.9774, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 79, "metric_value": 0.9943, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 73, "metric_value": 0.9934, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 65, "metric_value": 0.9957, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "relationship", "instances": 11, "metric_value": 0.9457, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 9, "metric_value": 0.7642, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Farming-fishing':
											# {"feature": "sex", "instances": 92, "metric_value": 0.6415, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "workclass", "instances": 89, "metric_value": 0.6544, "depth": 12}
												if obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 50, "metric_value": 0.469, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "race", "instances": 50, "metric_value": 0.469, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Private':
													# {"feature": "race", "instances": 21, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "relationship", "instances": 20, "metric_value": 0.9341, "depth": 14}
														if obj[7] == 'Husband':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Other':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "relationship", "instances": 10, "metric_value": 0.7219, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "race", "instances": 10, "metric_value": 0.7219, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												elif obj[1] == 'Without-pay':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											# {"feature": "workclass", "instances": 69, "metric_value": 0.6666, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 61, "metric_value": 0.5606, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 59, "metric_value": 0.5726, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 54, "metric_value": 0.5564, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Other':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Priv-house-serv':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Mexico':
										# {"feature": "sex", "instances": 23, "metric_value": 0.5586, "depth": 10}
										if obj[9] == 'Male':
											# {"feature": "workclass", "instances": 22, "metric_value": 0.4395, "depth": 11}
											if obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											else: return '>50K'
										elif obj[9] == 'Female':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Philippines':
										# {"feature": "race", "instances": 17, "metric_value": 0.9975, "depth": 10}
										if obj[8] == 'Asian-Pac-Islander':
											# {"feature": "workclass", "instances": 15, "metric_value": 0.971, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 13, "metric_value": 0.9612, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '>50K'
												elif obj[6] == 'Prof-specialty':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'White':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Germany':
										# {"feature": "relationship", "instances": 15, "metric_value": 0.9968, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "occupation", "instances": 14, "metric_value": 0.9852, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Sales':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '>50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '>50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Wife':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Puerto-Rico':
										# {"feature": "workclass", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 10, "metric_value": 0.7219, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Wife':
													return '>50K'
												elif obj[7] == 'Husband':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Federal-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Canada':
										# {"feature": "occupation", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[6] == 'Adm-clerical':
											return '>50K'
										elif obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											return '>50K'
										elif obj[6] == 'Handlers-cleaners':
											return '>50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '>50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Jamaica':
										# {"feature": "relationship", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "occupation", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '>50K'
											elif obj[6] == 'Tech-support':
												return '>50K'
											elif obj[6] == 'Adm-clerical':
												return '>50K'
											elif obj[6] == 'Prof-specialty':
												return '>50K'
											else: return '>50K'
										elif obj[7] == 'Wife':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'El-Salvador':
										# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[9] == 'Male':
											return '<=50K'
										elif obj[9] == 'Female':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Cuba':
										return '>50K'
									elif obj[13] == 'Poland':
										# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'South':
										# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Columbia':
										return '<=50K'
									elif obj[13] == 'Vietnam':
										return '<=50K'
									elif obj[13] == 'Haiti':
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Trinadad&Tobago':
										return '<=50K'
									elif obj[13] == 'Japan':
										return '<=50K'
									elif obj[13] == 'Peru':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Scotland':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'England':
										return '>50K'
									elif obj[13] == 'Italy':
										return '<=50K'
									elif obj[13] == 'Dominican-Republic':
										return '<=50K'
									elif obj[13] == 'Laos':
										return '<=50K'
									elif obj[13] == 'India':
										return '<=50K'
									elif obj[13] == 'Cambodia':
										return '>50K'
									elif obj[13] == 'Taiwan':
										return '<=50K'
									elif obj[13] == 'Nicaragua':
										return '<=50K'
									elif obj[13] == 'Guatemala':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Federal-gov':
											return '>50K'
										elif obj[1] == 'Private':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Greece':
										return '<=50K'
									elif obj[13] == 'Thailand':
										return '>50K'
									elif obj[13] == 'China':
										return '<=50K'
									elif obj[13] == 'France':
										return '>50K'
									elif obj[13] == 'Hong':
										return '<=50K'
									elif obj[13] == 'Iran':
										return '>50K'
									elif obj[13] == 'Yugoslavia':
										return '>50K'
									elif obj[13] == 'Ecuador':
										return '>50K'
									else: return '>50K'
								elif float(obj[12])<=1:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Bachelors':
								# {"feature": "hours-per-week", "instances": 2382, "metric_value": 0.9537, "depth": 8}
								if float(obj[12])>2:
									# {"feature": "native-country", "instances": 2380, "metric_value": 0.9533, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "relationship", "instances": 2167, "metric_value": 0.9464, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "occupation", "instances": 1906, "metric_value": 0.9439, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "workclass", "instances": 571, "metric_value": 0.8064, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 387, "metric_value": 0.7548, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 369, "metric_value": 0.7492, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 14, "metric_value": 0.7496, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "race", "instances": 61, "metric_value": 0.8047, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 61, "metric_value": 0.8047, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "race", "instances": 46, "metric_value": 0.9945, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 45, "metric_value": 0.9911, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													# {"feature": "race", "instances": 33, "metric_value": 0.8454, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 30, "metric_value": 0.8366, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "race", "instances": 27, "metric_value": 0.6913, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 24, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 17, "metric_value": 0.9774, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 13, "metric_value": 0.9957, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "race", "instances": 520, "metric_value": 0.9687, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 496, "metric_value": 0.968, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 324, "metric_value": 0.9578, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 64, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 36, "metric_value": 0.9978, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'State-gov':
														# {"feature": "sex", "instances": 30, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 26, "metric_value": 0.7793, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 16, "metric_value": 0.9544, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													# {"feature": "workclass", "instances": 13, "metric_value": 0.9957, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													# {"feature": "workclass", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Other':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Sales':
												# {"feature": "race", "instances": 335, "metric_value": 0.9307, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 323, "metric_value": 0.9339, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 233, "metric_value": 0.911, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 43, "metric_value": 0.8542, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 42, "metric_value": 0.9984, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														return '>50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "workclass", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												elif obj[8] == 'Other':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "workclass", "instances": 117, "metric_value": 0.9995, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 79, "metric_value": 0.9804, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 76, "metric_value": 0.9819, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "race", "instances": 21, "metric_value": 0.8631, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 21, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "race", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												elif obj[1] == 'State-gov':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "workclass", "instances": 92, "metric_value": 0.9583, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 55, "metric_value": 0.9457, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 53, "metric_value": 0.9562, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "race", "instances": 13, "metric_value": 0.9957, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 12, "metric_value": 0.9799, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "race", "instances": 11, "metric_value": 0.8454, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 9, "metric_value": 0.7642, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9911, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Tech-support':
												# {"feature": "workclass", "instances": 71, "metric_value": 0.9359, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 58, "metric_value": 0.9294, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 56, "metric_value": 0.9241, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												elif obj[1] == 'Self-emp-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Protective-serv':
												# {"feature": "workclass", "instances": 53, "metric_value": 0.8836, "depth": 12}
												if obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 30, "metric_value": 0.8366, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 25, "metric_value": 0.8555, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "race", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Private':
													# {"feature": "race", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Farming-fishing':
												# {"feature": "race", "instances": 44, "metric_value": 0.9257, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 43, "metric_value": 0.9103, "depth": 13}
													if obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 27, "metric_value": 0.7642, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Private':
														# {"feature": "sex", "instances": 11, "metric_value": 0.8454, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '>50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "race", "instances": 30, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 27, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 23, "metric_value": 0.9321, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "race", "instances": 29, "metric_value": 0.9784, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 25, "metric_value": 0.9896, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 20, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Other-service':
												# {"feature": "workclass", "instances": 27, "metric_value": 0.9751, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 23, "metric_value": 0.9656, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 18, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												# {"feature": "race", "instances": 17, "metric_value": 0.9367, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 15, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 12, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Wife':
											# {"feature": "race", "instances": 236, "metric_value": 0.9279, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 212, "metric_value": 0.9151, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "workclass", "instances": 99, "metric_value": 0.9079, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 53, "metric_value": 0.9414, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 37, "metric_value": 0.8419, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "sex", "instances": 51, "metric_value": 0.8479, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "workclass", "instances": 50, "metric_value": 0.8555, "depth": 14}
														if obj[1] == 'Private':
															return '>50K'
														elif obj[1] == 'State-gov':
															return '>50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '>50K'
														elif obj[1] == 'Federal-gov':
															return '<=50K'
														elif obj[1] == 'Self-emp-inc':
															return '>50K'
														elif obj[1] == 'Local-gov':
															return '>50K'
														else: return '>50K'
													elif obj[9] == 'Male':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "workclass", "instances": 26, "metric_value": 0.9829, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 17, "metric_value": 0.9774, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Sales':
													# {"feature": "sex", "instances": 17, "metric_value": 0.9367, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "workclass", "instances": 16, "metric_value": 0.896, "depth": 14}
														if obj[1] == 'Private':
															return '>50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '<=50K'
														elif obj[1] == 'Self-emp-inc':
															return '>50K'
														else: return '>50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Tech-support':
													return '>50K'
												elif obj[6] == 'Other-service':
													# {"feature": "workclass", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "occupation", "instances": 18, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "workclass", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Private':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Protective-serv':
													return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Asian-Pac-Islander':
												# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[6] == 'Other-service':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '>50K'
											elif obj[8] == 'Other':
												return '>50K'
											else: return '>50K'
										elif obj[7] == 'Other-relative':
											# {"feature": "occupation", "instances": 13, "metric_value": 0.3912, "depth": 11}
											if obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Priv-house-serv':
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Own-child':
											# {"feature": "occupation", "instances": 11, "metric_value": 0.9457, "depth": 11}
											if obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Handlers-cleaners':
												return '>50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '>50K'
											elif obj[6] == 'Tech-support':
												return '>50K'
											else: return '>50K'
										elif obj[7] == 'Not-in-family':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Philippines':
										# {"feature": "race", "instances": 37, "metric_value": 0.8419, "depth": 10}
										if obj[8] == 'Asian-Pac-Islander':
											# {"feature": "relationship", "instances": 35, "metric_value": 0.8631, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 25, "metric_value": 0.795, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "occupation", "instances": 17, "metric_value": 0.7871, "depth": 13}
													if obj[6] == 'Adm-clerical':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Exec-managerial':
														return '>50K'
													elif obj[6] == 'Prof-specialty':
														return '>50K'
													elif obj[6] == 'Other-service':
														return '>50K'
													elif obj[6] == 'Tech-support':
														return '>50K'
													elif obj[6] == 'Protective-serv':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[6] == 'Craft-repair':
														return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '>50K'
													elif obj[6] == 'Exec-managerial':
														return '>50K'
													elif obj[6] == 'Sales':
														return '>50K'
													elif obj[6] == 'Prof-specialty':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Wife':
												# {"feature": "occupation", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[6] == 'Adm-clerical':
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Private':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Other-service':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											elif obj[7] == 'Own-child':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'White':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Canada':
										# {"feature": "occupation", "instances": 15, "metric_value": 0.971, "depth": 10}
										if obj[6] == 'Prof-specialty':
											# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											return '>50K'
										elif obj[6] == 'Exec-managerial':
											return '>50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '>50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Germany':
										# {"feature": "workclass", "instances": 14, "metric_value": 0.9403, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 10, "metric_value": 0.971, "depth": 11}
											if obj[6] == 'Prof-specialty':
												# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Wife':
													return '<=50K'
												elif obj[7] == 'Husband':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Craft-repair':
												return '>50K'
											elif obj[6] == 'Machine-op-inspct':
												return '>50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Sales':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Federal-gov':
											return '>50K'
										elif obj[1] == 'Local-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'India':
										# {"feature": "relationship", "instances": 14, "metric_value": 0.9852, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "workclass", "instances": 11, "metric_value": 0.994, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[6] == 'Exec-managerial':
													return '>50K'
												elif obj[6] == 'Sales':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Asian-Pac-Islander':
														return '<=50K'
													elif obj[8] == 'White':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '>50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Other-relative':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Japan':
										# {"feature": "race", "instances": 13, "metric_value": 0.9612, "depth": 10}
										if obj[8] == 'Asian-Pac-Islander':
											# {"feature": "workclass", "instances": 11, "metric_value": 0.8454, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 9, "metric_value": 0.7642, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "occupation", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[6] == 'Exec-managerial':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Craft-repair':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'White':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Mexico':
										# {"feature": "workclass", "instances": 12, "metric_value": 0.9799, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Sales':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										elif obj[1] == 'Local-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'China':
										# {"feature": "occupation", "instances": 12, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Exec-managerial':
											return '>50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'England':
										# {"feature": "occupation", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[6] == 'Exec-managerial':
											return '>50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '>50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'South':
										# {"feature": "workclass", "instances": 11, "metric_value": 0.684, "depth": 10}
										if obj[1] == 'Self-emp-not-inc':
											# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Sales':
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[13] == 'Iran':
										# {"feature": "workclass", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "race", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Exec-managerial':
													return '>50K'
												elif obj[6] == 'Adm-clerical':
													return '>50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Italy':
										# {"feature": "workclass", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[6] == 'Prof-specialty':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Handlers-cleaners':
												return '>50K'
											elif obj[6] == 'Exec-managerial':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'State-gov':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Puerto-Rico':
										# {"feature": "workclass", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										elif obj[1] == 'State-gov':
											return '>50K'
										elif obj[1] == 'Federal-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Cuba':
										# {"feature": "workclass", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[7] == 'Wife':
												# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Husband':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										elif obj[1] == 'Local-gov':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Vietnam':
										# {"feature": "occupation", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Poland':
										# {"feature": "occupation", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											return '>50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Taiwan':
										# {"feature": "workclass", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7] == 'Wife':
												return '>50K'
											elif obj[7] == 'Husband':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Yugoslavia':
										# {"feature": "occupation", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Exec-managerial':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Ireland':
										return '>50K'
									elif obj[13] == 'Jamaica':
										return '<=50K'
									elif obj[13] == 'Ecuador':
										return '<=50K'
									elif obj[13] == 'Haiti':
										return '>50K'
									elif obj[13] == 'France':
										return '>50K'
									elif obj[13] == 'Greece':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										else: return '>50K'
									elif obj[13] == 'El-Salvador':
										return '<=50K'
									elif obj[13] == 'Thailand':
										return '<=50K'
									elif obj[13] == 'Dominican-Republic':
										return '<=50K'
									elif obj[13] == 'Nicaragua':
										return '<=50K'
									elif obj[13] == 'Hong':
										return '>50K'
									elif obj[13] == 'Cambodia':
										return '>50K'
									elif obj[13] == 'Peru':
										return '<=50K'
									elif obj[13] == 'Columbia':
										return '<=50K'
									elif obj[13] == 'Scotland':
										return '>50K'
									else: return '>50K'
								elif float(obj[12])<=2:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Masters':
								# {"feature": "hours-per-week", "instances": 811, "metric_value": 0.8485, "depth": 8}
								if float(obj[12])>1:
									# {"feature": "native-country", "instances": 810, "metric_value": 0.8473, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "occupation", "instances": 728, "metric_value": 0.8262, "depth": 10}
										if obj[6] == 'Prof-specialty':
											# {"feature": "race", "instances": 361, "metric_value": 0.8475, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "sex", "instances": 341, "metric_value": 0.8454, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "relationship", "instances": 287, "metric_value": 0.8766, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "workclass", "instances": 285, "metric_value": 0.8748, "depth": 14}
														if obj[1] == 'Private':
															return '>50K'
														elif obj[1] == 'Local-gov':
															return '>50K'
														elif obj[1] == 'State-gov':
															return '>50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '>50K'
														elif obj[1] == 'Federal-gov':
															return '>50K'
														elif obj[1] == 'Self-emp-inc':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Other-relative':
														# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1] == 'Private':
															return '>50K'
														elif obj[1] == 'Local-gov':
															return '<=50K'
														else: return '<=50K'
													else: return '>50K'
												elif obj[9] == 'Female':
													# {"feature": "workclass", "instances": 54, "metric_value": 0.6052, "depth": 13}
													if obj[1] == 'Local-gov':
														# {"feature": "relationship", "instances": 29, "metric_value": 0.5788, "depth": 14}
														if obj[7] == 'Wife':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Private':
														# {"feature": "relationship", "instances": 16, "metric_value": 0.8113, "depth": 14}
														if obj[7] == 'Wife':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													elif obj[1] == 'Self-emp-inc':
														return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												# {"feature": "relationship", "instances": 14, "metric_value": 0.5917, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "workclass", "instances": 12, "metric_value": 0.65, "depth": 13}
													if obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Private':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Asian-Pac-Islander':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Other':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'State-gov':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "relationship", "instances": 227, "metric_value": 0.6309, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 212, "metric_value": 0.6003, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 199, "metric_value": 0.5728, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 125, "metric_value": 0.4562, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 21, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'State-gov':
														# {"feature": "sex", "instances": 15, "metric_value": 0.8366, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 14, "metric_value": 0.7496, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 14, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 10, "metric_value": 0.469, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													# {"feature": "workclass", "instances": 8, "metric_value": 0.9544, "depth": 13}
													if obj[1] == 'Local-gov':
														return '>50K'
													elif obj[1] == 'Private':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												# {"feature": "race", "instances": 15, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 14, "metric_value": 0.9403, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 10, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'State-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													elif obj[1] == 'Self-emp-inc':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[6] == 'Sales':
											# {"feature": "relationship", "instances": 66, "metric_value": 0.866, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 64, "metric_value": 0.8571, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 62, "metric_value": 0.8474, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 32, "metric_value": 0.8571, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 17, "metric_value": 0.6723, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 12, "metric_value": 0.9799, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Self-emp-not-inc':
														return '>50K'
													elif obj[1] == 'Private':
														return '<=50K'
													else: return '<=50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "relationship", "instances": 22, "metric_value": 0.976, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 20, "metric_value": 0.9928, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 19, "metric_value": 0.998, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9911, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'State-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 13, "metric_value": 0.9957, "depth": 11}
											if obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 8, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 8, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Private':
												return '>50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Tech-support':
											# {"feature": "workclass", "instances": 12, "metric_value": 0.8113, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 10, "metric_value": 0.8813, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Farming-fishing':
											# {"feature": "workclass", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Private':
												return '>50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Other-service':
											# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[8] == 'White':
												return '>50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'India':
										# {"feature": "race", "instances": 17, "metric_value": 0.9975, "depth": 10}
										if obj[8] == 'Asian-Pac-Islander':
											# {"feature": "workclass", "instances": 15, "metric_value": 0.971, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 11, "metric_value": 0.9457, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "relationship", "instances": 8, "metric_value": 0.9544, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'State-gov':
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'White':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Taiwan':
										# {"feature": "workclass", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[1] == 'Private':
											return '>50K'
										elif obj[1] == 'State-gov':
											return '<=50K'
										elif obj[1] == 'Local-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'England':
										# {"feature": "occupation", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[6] == 'Prof-specialty':
											# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Exec-managerial':
											return '>50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'China':
										# {"feature": "relationship", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "workclass", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'State-gov':
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Wife':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Canada':
										# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == 'Exec-managerial':
												return '>50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'State-gov':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Philippines':
										# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[7] == 'Husband':
												return '>50K'
											elif obj[7] == 'Wife':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Mexico':
										# {"feature": "workclass", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'South':
										# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Cuba':
										return '>50K'
									elif obj[13] == 'Iran':
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Prof-specialty':
											return '>50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Japan':
										# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8] == 'Asian-Pac-Islander':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Exec-managerial':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[8] == 'White':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'France':
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Exec-managerial':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Hong':
										return '>50K'
									elif obj[13] == 'Poland':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Local-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'El-Salvador':
										return '>50K'
									elif obj[13] == 'Italy':
										return '>50K'
									elif obj[13] == 'Ecuador':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Nicaragua':
										return '<=50K'
									elif obj[13] == 'Germany':
										return '<=50K'
									elif obj[13] == 'Portugal':
										return '>50K'
									elif obj[13] == 'Jamaica':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[12])<=1:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Assoc-voc':
								# {"feature": "hours-per-week", "instances": 640, "metric_value": 0.9887, "depth": 8}
								if float(obj[12])>9.79937015875067:
									# {"feature": "native-country", "instances": 636, "metric_value": 0.9897, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "occupation", "instances": 591, "metric_value": 0.9907, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "relationship", "instances": 145, "metric_value": 0.9848, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 144, "metric_value": 0.986, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 130, "metric_value": 0.971, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 105, "metric_value": 0.981, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "workclass", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Local-gov':
														return '>50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Private':
														return '>50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													else: return '<=50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Prof-specialty':
											# {"feature": "race", "instances": 77, "metric_value": 0.9793, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 71, "metric_value": 0.9757, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 56, "metric_value": 0.9544, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 39, "metric_value": 0.9418, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 14, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Own-child':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Wife':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Husband':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Wife':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'Other':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "relationship", "instances": 74, "metric_value": 0.966, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 63, "metric_value": 0.9852, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 38, "metric_value": 0.9678, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 36, "metric_value": 0.9641, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "race", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "race", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Wife':
												# {"feature": "race", "instances": 10, "metric_value": 0.7219, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Other-relative':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Tech-support':
											# {"feature": "workclass", "instances": 47, "metric_value": 0.9441, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 38, "metric_value": 0.8997, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 30, "metric_value": 0.9481, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 30, "metric_value": 0.9481, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													# {"feature": "race", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "workclass", "instances": 44, "metric_value": 0.8757, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 40, "metric_value": 0.8485, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 25, "metric_value": 0.795, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 23, "metric_value": 0.7554, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													# {"feature": "race", "instances": 14, "metric_value": 0.9403, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 11, "metric_value": 0.9457, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													return '>50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											# {"feature": "relationship", "instances": 44, "metric_value": 0.9865, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 43, "metric_value": 0.9808, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 35, "metric_value": 0.9275, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 35, "metric_value": 0.9275, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "race", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Farming-fishing':
											# {"feature": "workclass", "instances": 36, "metric_value": 0.7642, "depth": 11}
											if obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 26, "metric_value": 0.7063, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 26, "metric_value": 0.7063, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 26, "metric_value": 0.7063, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Private':
												# {"feature": "relationship", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											# {"feature": "workclass", "instances": 30, "metric_value": 0.9481, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 29, "metric_value": 0.9294, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 27, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 26, "metric_value": 0.9306, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Other-service':
											# {"feature": "workclass", "instances": 28, "metric_value": 0.7496, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 21, "metric_value": 0.7919, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 17, "metric_value": 0.6723, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 17, "metric_value": 0.6723, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'White':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "race", "instances": 26, "metric_value": 0.8905, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 23, "metric_value": 0.9321, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 20, "metric_value": 0.8813, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 19, "metric_value": 0.8997, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "race", "instances": 25, "metric_value": 0.9988, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 23, "metric_value": 0.9877, "depth": 12}
												if obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 12, "metric_value": 0.65, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 12, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "relationship", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Private':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											# {"feature": "race", "instances": 15, "metric_value": 0.5665, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 13, "metric_value": 0.6194, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 12, "metric_value": 0.65, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 12, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Germany':
										# {"feature": "occupation", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[6] == 'Sales':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '>50K'
										elif obj[6] == 'Transport-moving':
											return '>50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										elif obj[6] == 'Other-service':
											return '>50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Mexico':
										# {"feature": "occupation", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Canada':
										# {"feature": "occupation", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[6] == 'Tech-support':
											return '>50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Greece':
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Philippines':
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Prof-specialty':
											return '>50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'India':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'England':
										return '<=50K'
									elif obj[13] == 'Puerto-Rico':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Hong':
										return '<=50K'
									elif obj[13] == 'Jamaica':
										return '<=50K'
									elif obj[13] == 'Guatemala':
										return '<=50K'
									elif obj[13] == 'Hungary':
										return '>50K'
									elif obj[13] == 'Yugoslavia':
										return '<=50K'
									elif obj[13] == 'Laos':
										return '<=50K'
									elif obj[13] == 'Nicaragua':
										return '>50K'
									elif obj[13] == 'Poland':
										return '>50K'
									elif obj[13] == 'Italy':
										return '<=50K'
									elif obj[13] == 'Columbia':
										return '<=50K'
									elif obj[13] == 'Vietnam':
										return '<=50K'
									elif obj[13] == 'Japan':
										return '<=50K'
									elif obj[13] == 'Peru':
										return '<=50K'
									elif obj[13] == 'Portugal':
										return '>50K'
									elif obj[13] == 'Ecuador':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[12])<=9.79937015875067:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Assoc-acdm':
								# {"feature": "hours-per-week", "instances": 416, "metric_value": 0.9962, "depth": 8}
								if float(obj[12])>2:
									# {"feature": "native-country", "instances": 414, "metric_value": 0.9957, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "relationship", "instances": 378, "metric_value": 0.998, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "occupation", "instances": 314, "metric_value": 0.9976, "depth": 11}
											if obj[6] == 'Sales':
												# {"feature": "race", "instances": 51, "metric_value": 0.9975, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 48, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 33, "metric_value": 0.994, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "race", "instances": 49, "metric_value": 0.8631, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 46, "metric_value": 0.859, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 33, "metric_value": 0.799, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "race", "instances": 47, "metric_value": 0.9601, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 46, "metric_value": 0.9503, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 37, "metric_value": 0.9569, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "workclass", "instances": 43, "metric_value": 0.9996, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 33, "metric_value": 0.9993, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 30, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Tech-support':
												# {"feature": "race", "instances": 29, "metric_value": 0.9991, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 26, "metric_value": 0.9829, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 20, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "race", "instances": 28, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 27, "metric_value": 0.999, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 15, "metric_value": 0.9968, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													elif obj[1] == 'State-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Protective-serv':
												# {"feature": "workclass", "instances": 18, "metric_value": 0.9911, "depth": 12}
												if obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 10, "metric_value": 0.8813, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Private':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "workclass", "instances": 14, "metric_value": 0.9852, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 13, "metric_value": 0.9612, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 12, "metric_value": 0.9799, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "workclass", "instances": 12, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												# {"feature": "race", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Without-pay':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												# {"feature": "race", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Private':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif obj[7] == 'Wife':
											# {"feature": "occupation", "instances": 59, "metric_value": 0.9998, "depth": 11}
											if obj[6] == 'Adm-clerical':
												# {"feature": "workclass", "instances": 19, "metric_value": 0.9819, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												elif obj[1] == 'Self-emp-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "race", "instances": 13, "metric_value": 0.9612, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 12, "metric_value": 0.9799, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "workclass", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												# {"feature": "workclass", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[8] == 'White':
													return '<=50K'
												elif obj[8] == 'Other':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '>50K'
											elif obj[6] == 'Transport-moving':
												return '>50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Own-child':
											return '<=50K'
										elif obj[7] == 'Not-in-family':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Italy':
										# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7] == 'Husband':
											return '<=50K'
										elif obj[7] == 'Wife':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'India':
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Adm-clerical':
											# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Husband':
												return '<=50K'
											elif obj[7] == 'Wife':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Exec-managerial':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'El-Salvador':
										return '<=50K'
									elif obj[13] == 'Haiti':
										return '<=50K'
									elif obj[13] == 'Iran':
										return '<=50K'
									elif obj[13] == 'France':
										return '>50K'
									elif obj[13] == 'Mexico':
										return '<=50K'
									elif obj[13] == 'Puerto-Rico':
										return '<=50K'
									elif obj[13] == 'Yugoslavia':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Machine-op-inspct':
											return '>50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Columbia':
										return '<=50K'
									elif obj[13] == 'Germany':
										return '>50K'
									elif obj[13] == 'Poland':
										return '<=50K'
									elif obj[13] == 'England':
										return '>50K'
									elif obj[13] == 'Cuba':
										return '<=50K'
									elif obj[13] == 'Hungary':
										return '<=50K'
									elif obj[13] == 'Nicaragua':
										return '<=50K'
									elif obj[13] == 'Philippines':
										return '<=50K'
									elif obj[13] == 'Portugal':
										return '<=50K'
									elif obj[13] == 'Hong':
										return '>50K'
									elif obj[13] == 'Canada':
										return '>50K'
									elif obj[13] == 'Thailand':
										return '>50K'
									elif obj[13] == 'Jamaica':
										return '<=50K'
									elif obj[13] == 'Japan':
										return '>50K'
									else: return '>50K'
								elif float(obj[12])<=2:
									return '>50K'
								else: return '>50K'
							elif obj[3] == '7th-8th':
								# {"feature": "hours-per-week", "instances": 345, "metric_value": 0.4456, "depth": 8}
								if float(obj[12])<=55.40473980582912:
									# {"feature": "native-country", "instances": 312, "metric_value": 0.3912, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "workclass", "instances": 253, "metric_value": 0.3988, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 175, "metric_value": 0.2924, "depth": 11}
											if obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "race", "instances": 31, "metric_value": 0.3451, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 29, "metric_value": 0.3621, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 28, "metric_value": 0.3712, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "race", "instances": 31, "metric_value": 0.3451, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 24, "metric_value": 0.4138, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 21, "metric_value": 0.4537, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Other':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												# {"feature": "race", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "relationship", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														return '>50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "occupation", "instances": 49, "metric_value": 0.5917, "depth": 11}
											if obj[6] == 'Craft-repair':
												# {"feature": "race", "instances": 15, "metric_value": 0.3534, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 14, "metric_value": 0.3712, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 14, "metric_value": 0.3712, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "relationship", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Local-gov':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											# {"feature": "occupation", "instances": 9, "metric_value": 0.9911, "depth": 11}
											if obj[6] == 'Craft-repair':
												# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '>50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'State-gov':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Mexico':
										# {"feature": "occupation", "instances": 27, "metric_value": 0.2285, "depth": 10}
										if obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Puerto-Rico':
										return '<=50K'
									elif obj[13] == 'Cuba':
										return '<=50K'
									elif obj[13] == 'China':
										return '<=50K'
									elif obj[13] == 'Dominican-Republic':
										return '<=50K'
									elif obj[13] == 'Portugal':
										return '<=50K'
									elif obj[13] == 'Poland':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'El-Salvador':
										return '<=50K'
									elif obj[13] == 'Italy':
										return '<=50K'
									elif obj[13] == 'Canada':
										return '>50K'
									elif obj[13] == 'Cambodia':
										return '<=50K'
									elif obj[13] == 'Hong':
										return '<=50K'
									elif obj[13] == 'Greece':
										return '>50K'
									elif obj[13] == 'South':
										return '<=50K'
									elif obj[13] == 'Ecuador':
										return '<=50K'
									elif obj[13] == 'Nicaragua':
										return '<=50K'
									elif obj[13] == 'Vietnam':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[12])>55.40473980582912:
									# {"feature": "race", "instances": 33, "metric_value": 0.799, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "occupation", "instances": 32, "metric_value": 0.7579, "depth": 10}
										if obj[6] == 'Farming-fishing':
											# {"feature": "workclass", "instances": 11, "metric_value": 0.8454, "depth": 11}
											if obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 9, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Private':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[1] == 'Private':
												return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Self-emp-not-inc':
												# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[13] == 'Greece':
													return '<=50K'
												elif obj[13] == 'United-States':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Private':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										else: return '<=50K'
									elif obj[8] == 'Black':
										return '>50K'
									else: return '>50K'
								else: return '<=50K'
							elif obj[3] == '11th':
								# {"feature": "hours-per-week", "instances": 339, "metric_value": 0.5236, "depth": 8}
								if float(obj[12])>29.15014795846047:
									# {"feature": "native-country", "instances": 303, "metric_value": 0.5629, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "relationship", "instances": 279, "metric_value": 0.5837, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "workclass", "instances": 252, "metric_value": 0.5813, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 209, "metric_value": 0.5682, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "race", "instances": 63, "metric_value": 0.5491, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 62, "metric_value": 0.5548, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "race", "instances": 35, "metric_value": 0.422, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 33, "metric_value": 0.4395, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Transport-moving':
													# {"feature": "race", "instances": 31, "metric_value": 0.3451, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 28, "metric_value": 0.3712, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													# {"feature": "race", "instances": 16, "metric_value": 0.896, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 13, "metric_value": 0.8905, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Other':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													# {"feature": "race", "instances": 16, "metric_value": 0.5436, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 12, "metric_value": 0.4138, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													# {"feature": "race", "instances": 13, "metric_value": 0.7793, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 13, "metric_value": 0.7793, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "race", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Protective-serv':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "occupation", "instances": 25, "metric_value": 0.5294, "depth": 12}
												if obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Transport-moving':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "occupation", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[6] == 'Transport-moving':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[6] == 'Transport-moving':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Craft-repair':
													return '>50K'
												elif obj[6] == 'Exec-managerial':
													return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[7] == 'Wife':
											# {"feature": "race", "instances": 18, "metric_value": 0.65, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 14, "metric_value": 0.3712, "depth": 12}
												if obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "occupation", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Other-service':
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Own-child':
											return '<=50K'
										elif obj[7] == 'Other-relative':
											return '<=50K'
										elif obj[7] == 'Not-in-family':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Mexico':
										return '<=50K'
									elif obj[13] == 'Dominican-Republic':
										return '<=50K'
									elif obj[13] == 'Cuba':
										return '<=50K'
									elif obj[13] == 'Vietnam':
										return '<=50K'
									elif obj[13] == 'Philippines':
										return '<=50K'
									elif obj[13] == 'El-Salvador':
										return '<=50K'
									elif obj[13] == 'Hong':
										return '<=50K'
									elif obj[13] == 'Puerto-Rico':
										return '<=50K'
									elif obj[13] == 'Laos':
										return '<=50K'
									elif obj[13] == 'Poland':
										return '>50K'
									elif obj[13] == 'Guatemala':
										return '<=50K'
									elif obj[13] == 'Columbia':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[12])<=29.15014795846047:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == '10th':
								# {"feature": "native-country", "instances": 336, "metric_value": 0.5681, "depth": 8}
								if obj[13] == 'United-States':
									# {"feature": "sex", "instances": 314, "metric_value": 0.5762, "depth": 9}
									if obj[9] == 'Male':
										# {"feature": "relationship", "instances": 288, "metric_value": 0.6081, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "hours-per-week", "instances": 285, "metric_value": 0.6032, "depth": 11}
											if float(obj[12])>6.36934388386419:
												# {"feature": "occupation", "instances": 283, "metric_value": 0.6058, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "workclass", "instances": 91, "metric_value": 0.6458, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 66, "metric_value": 0.7158, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "race", "instances": 15, "metric_value": 0.5665, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Transport-moving':
													# {"feature": "workclass", "instances": 48, "metric_value": 0.8427, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 40, "metric_value": 0.8813, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '>50K'
														elif obj[8] == 'Amer-Indian-Eskimo':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "race", "instances": 40, "metric_value": 0.5436, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "workclass", "instances": 37, "metric_value": 0.5714, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													# {"feature": "race", "instances": 21, "metric_value": 0.2762, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "workclass", "instances": 17, "metric_value": 0.3228, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'State-gov':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Sales':
													# {"feature": "workclass", "instances": 15, "metric_value": 0.3534, "depth": 13}
													if obj[1] == 'Private':
														return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "workclass", "instances": 14, "metric_value": 0.8631, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													elif obj[1] == 'State-gov':
														return '>50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "workclass", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 10, "metric_value": 0.469, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Amer-Indian-Eskimo':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Protective-serv':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '>50K'
												else: return '>50K'
											elif float(obj[12])<=6.36934388386419:
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Own-child':
											# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8] == 'Other':
												return '>50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Other-relative':
											return '<=50K'
										else: return '<=50K'
									elif obj[9] == 'Female':
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'Mexico':
									return '<=50K'
								elif obj[13] == 'Guatemala':
									return '<=50K'
								elif obj[13] == 'Cuba':
									# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6] == 'Other-service':
										return '>50K'
									elif obj[6] == 'Prof-specialty':
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'Portugal':
									return '<=50K'
								elif obj[13] == 'China':
									return '<=50K'
								elif obj[13] == 'Japan':
									return '>50K'
								elif obj[13] == 'India':
									return '<=50K'
								elif obj[13] == 'Puerto-Rico':
									return '<=50K'
								elif obj[13] == 'El-Salvador':
									return '<=50K'
								elif obj[13] == 'Yugoslavia':
									return '<=50K'
								elif obj[13] == 'Vietnam':
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == '9th':
								# {"feature": "hours-per-week", "instances": 226, "metric_value": 0.4164, "depth": 8}
								if float(obj[12])<=50.66403924678729:
									# {"feature": "relationship", "instances": 212, "metric_value": 0.3687, "depth": 9}
									if obj[7] == 'Husband':
										# {"feature": "native-country", "instances": 185, "metric_value": 0.3253, "depth": 10}
										if obj[13] == 'United-States':
											# {"feature": "workclass", "instances": 155, "metric_value": 0.3451, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 119, "metric_value": 0.3228, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "race", "instances": 30, "metric_value": 0.3534, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 28, "metric_value": 0.2223, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "race", "instances": 21, "metric_value": 0.2762, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 17, "metric_value": 0.3228, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Transport-moving':
													return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													# {"feature": "race", "instances": 14, "metric_value": 0.3712, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 13, "metric_value": 0.3912, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 13, "metric_value": 0.3912, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 10, "metric_value": 0.469, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Black':
														return '>50K'
													elif obj[8] == 'White':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Protective-serv':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "occupation", "instances": 18, "metric_value": 0.5033, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "race", "instances": 13, "metric_value": 0.3912, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 13, "metric_value": 0.3912, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Farming-fishing':
													# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[13] == 'Mexico':
											return '<=50K'
										elif obj[13] == 'Guatemala':
											return '<=50K'
										elif obj[13] == 'Trinadad&Tobago':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '>50K'
											else: return '>50K'
										elif obj[13] == 'Canada':
											return '<=50K'
										elif obj[13] == 'Portugal':
											return '<=50K'
										elif obj[13] == 'Dominican-Republic':
											return '<=50K'
										elif obj[13] == 'Puerto-Rico':
											return '<=50K'
										elif obj[13] == 'India':
											return '<=50K'
										elif obj[13] == 'Poland':
											return '<=50K'
										else: return '<=50K'
									elif obj[7] == 'Wife':
										# {"feature": "native-country", "instances": 20, "metric_value": 0.6098, "depth": 10}
										if obj[13] == 'United-States':
											# {"feature": "race", "instances": 15, "metric_value": 0.5665, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[6] == 'Machine-op-inspct':
													# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '>50K'
											else: return '>50K'
										elif obj[13] == 'Portugal':
											return '<=50K'
										elif obj[13] == 'Yugoslavia':
											return '>50K'
										elif obj[13] == 'Hong':
											return '<=50K'
										elif obj[13] == 'Haiti':
											return '<=50K'
										else: return '<=50K'
									elif obj[7] == 'Other-relative':
										return '<=50K'
									elif obj[7] == 'Own-child':
										return '>50K'
									else: return '>50K'
								elif float(obj[12])>50.66403924678729:
									# {"feature": "occupation", "instances": 14, "metric_value": 0.8631, "depth": 9}
									if obj[6] == 'Transport-moving':
										# {"feature": "workclass", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Sales':
										# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7] == 'Husband':
											return '>50K'
										elif obj[7] == 'Wife':
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Craft-repair':
										return '<=50K'
									elif obj[6] == 'Farming-fishing':
										return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Other-service':
										return '<=50K'
									else: return '<=50K'
								else: return '<=50K'
							elif obj[3] == '5th-6th':
								# {"feature": "hours-per-week", "instances": 164, "metric_value": 0.4208, "depth": 8}
								if float(obj[12])<=69.55774526091733:
									# {"feature": "workclass", "instances": 161, "metric_value": 0.4048, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "native-country", "instances": 137, "metric_value": 0.321, "depth": 10}
										if obj[13] == 'Mexico':
											# {"feature": "occupation", "instances": 70, "metric_value": 0.108, "depth": 11}
											if obj[6] == 'Machine-op-inspct':
												# {"feature": "sex", "instances": 16, "metric_value": 0.3373, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "race", "instances": 14, "metric_value": 0.3712, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "relationship", "instances": 11, "metric_value": 0.4395, "depth": 14}
														if obj[7] == 'Husband':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Other':
														return '<=50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Female':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											else: return '<=50K'
										elif obj[13] == 'United-States':
											# {"feature": "occupation", "instances": 44, "metric_value": 0.3591, "depth": 11}
											if obj[6] == 'Prof-specialty':
												# {"feature": "race", "instances": 11, "metric_value": 0.4395, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Other':
													return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "race", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											else: return '<=50K'
										elif obj[13] == 'Italy':
											return '<=50K'
										elif obj[13] == 'Philippines':
											# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '>50K'
											else: return '>50K'
										elif obj[13] == 'El-Salvador':
											return '<=50K'
										elif obj[13] == 'Laos':
											# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Husband':
												return '<=50K'
											elif obj[7] == 'Wife':
												return '>50K'
											else: return '>50K'
										elif obj[13] == 'Vietnam':
											return '>50K'
										elif obj[13] == 'Haiti':
											return '<=50K'
										elif obj[13] == 'Jamaica':
											return '<=50K'
										elif obj[13] == 'Puerto-Rico':
											return '>50K'
										elif obj[13] == 'Trinadad&Tobago':
											return '<=50K'
										elif obj[13] == 'Guatemala':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										# {"feature": "occupation", "instances": 13, "metric_value": 0.7793, "depth": 10}
										if obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[13] == 'United-States':
												return '<=50K'
											elif obj[13] == 'Mexico':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '>50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Local-gov':
										return '<=50K'
									elif obj[1] == 'Self-emp-inc':
										# {"feature": "occupation", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '>50K'
										elif obj[6] == 'Craft-repair':
											return '>50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'State-gov':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[12])>69.55774526091733:
									# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '>50K'
									elif obj[6] == 'Farming-fishing':
										return '<=50K'
									else: return '<=50K'
								else: return '<=50K'
							elif obj[3] == '12th':
								# {"feature": "hours-per-week", "instances": 124, "metric_value": 0.7251, "depth": 8}
								if float(obj[12])>33:
									# {"feature": "native-country", "instances": 116, "metric_value": 0.7519, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "race", "instances": 92, "metric_value": 0.8113, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "occupation", "instances": 79, "metric_value": 0.7742, "depth": 11}
											if obj[6] == 'Craft-repair':
												# {"feature": "relationship", "instances": 31, "metric_value": 0.7706, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "workclass", "instances": 29, "metric_value": 0.7973, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 22, "metric_value": 0.8454, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												elif obj[7] == 'Not-in-family':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "workclass", "instances": 10, "metric_value": 0.7219, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												# {"feature": "workclass", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												return '>50K'
											elif obj[6] == 'Tech-support':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'State-gov':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Armed-Forces':
												return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'Black':
											# {"feature": "relationship", "instances": 10, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "occupation", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[6] == 'Adm-clerical':
														return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '>50K'
													elif obj[6] == 'Protective-serv':
														return '<=50K'
													elif obj[6] == 'Craft-repair':
														return '>50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Asian-Pac-Islander':
											return '<=50K'
										elif obj[8] == 'Other':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Mexico':
										return '<=50K'
									elif obj[13] == 'Dominican-Republic':
										return '<=50K'
									elif obj[13] == 'Jamaica':
										return '<=50K'
									elif obj[13] == 'Italy':
										return '<=50K'
									elif obj[13] == 'Cuba':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Germany':
										return '<=50K'
									elif obj[13] == 'Guatemala':
										return '<=50K'
									elif obj[13] == 'Ecuador':
										return '<=50K'
									elif obj[13] == 'Vietnam':
										return '<=50K'
									elif obj[13] == 'El-Salvador':
										return '<=50K'
									elif obj[13] == 'Columbia':
										return '<=50K'
									elif obj[13] == 'Cambodia':
										return '>50K'
									elif obj[13] == 'Puerto-Rico':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[12])<=33:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == '1st-4th':
								# {"feature": "hours-per-week", "instances": 78, "metric_value": 0.3912, "depth": 8}
								if float(obj[12])<=53.14727911510952:
									# {"feature": "occupation", "instances": 72, "metric_value": 0.3095, "depth": 9}
									if obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										# {"feature": "native-country", "instances": 12, "metric_value": 0.4138, "depth": 10}
										if obj[13] == 'Mexico':
											# {"feature": "relationship", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Wife':
												return '<=50K'
											else: return '<=50K'
										elif obj[13] == 'Italy':
											return '<=50K'
										elif obj[13] == 'United-States':
											return '<=50K'
										elif obj[13] == 'Portugal':
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Craft-repair':
										# {"feature": "race", "instances": 12, "metric_value": 0.65, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "native-country", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[13] == 'Mexico':
												# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[13] == 'United-States':
												return '<=50K'
											elif obj[13] == 'Portugal':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'Asian-Pac-Islander':
											return '<=50K'
										elif obj[8] == 'Other':
											return '<=50K'
										elif obj[8] == 'Black':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '<=50K'
									elif obj[6] == 'Transport-moving':
										return '<=50K'
									elif obj[6] == 'Farming-fishing':
										return '<=50K'
									elif obj[6] == 'Sales':
										return '<=50K'
									elif obj[6] == 'Exec-managerial':
										return '>50K'
									elif obj[6] == 'Protective-serv':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[12])>53.14727911510952:
									# {"feature": "workclass", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6] == 'Farming-fishing':
											# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'Mexico':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Self-emp-inc':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '>50K'
									else: return '>50K'
								else: return '<=50K'
							elif obj[3] == 'Preschool':
								return '<=50K'
							else: return '<=50K'
						elif float(obj[11])>1508.4669661576388:
							# {"feature": "hours-per-week", "instances": 806, "metric_value": 0.8846, "depth": 7}
							if float(obj[12])>4:
								# {"feature": "education", "instances": 805, "metric_value": 0.8836, "depth": 8}
								if obj[3] == 'HS-grad':
									# {"feature": "native-country", "instances": 221, "metric_value": 0.9922, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "occupation", "instances": 214, "metric_value": 0.9937, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "race", "instances": 60, "metric_value": 0.9871, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "sex", "instances": 57, "metric_value": 0.973, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "workclass", "instances": 55, "metric_value": 0.9806, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "relationship", "instances": 38, "metric_value": 0.998, "depth": 14}
														if obj[7] == 'Husband':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "relationship", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[7] == 'Husband':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[7] == 'Husband':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[7] == 'Husband':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Female':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '>50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Sales':
											# {"feature": "race", "instances": 30, "metric_value": 0.9481, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 28, "metric_value": 0.9059, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 18, "metric_value": 0.9911, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 18, "metric_value": 0.9911, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "workclass", "instances": 26, "metric_value": 0.5159, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 12, "metric_value": 0.65, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											elif obj[1] == 'Self-emp-inc':
												# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											elif obj[1] == 'Local-gov':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "race", "instances": 21, "metric_value": 0.9852, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 20, "metric_value": 0.971, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 17, "metric_value": 0.9774, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 17, "metric_value": 0.9774, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											# {"feature": "race", "instances": 17, "metric_value": 0.9975, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "relationship", "instances": 16, "metric_value": 0.9887, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "workclass", "instances": 15, "metric_value": 0.9968, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 15, "metric_value": 0.9968, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Wife':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Farming-fishing':
											# {"feature": "relationship", "instances": 15, "metric_value": 0.9183, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 14, "metric_value": 0.9403, "depth": 12}
												if obj[1] == 'Self-emp-not-inc':
													# {"feature": "race", "instances": 11, "metric_value": 0.9457, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 11, "metric_value": 0.9457, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Private':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Wife':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "workclass", "instances": 12, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[7] == 'Wife':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'Black':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'White':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Prof-specialty':
											# {"feature": "workclass", "instances": 12, "metric_value": 0.8113, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 9, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											elif obj[1] == 'Local-gov':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Other-service':
											# {"feature": "race", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Wife':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Husband':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'Private':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											# {"feature": "workclass", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Tech-support':
											return '>50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Local-gov':
												return '>50K'
											elif obj[1] == 'Private':
												return '<=50K'
											else: return '<=50K'
										else: return '>50K'
									elif obj[13] == 'Canada':
										return '>50K'
									elif obj[13] == 'Trinadad&Tobago':
										return '>50K'
									elif obj[13] == 'Vietnam':
										return '<=50K'
									elif obj[13] == 'Italy':
										return '>50K'
									elif obj[13] == 'Poland':
										return '<=50K'
									elif obj[13] == 'Iran':
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Bachelors':
									# {"feature": "native-country", "instances": 213, "metric_value": 0.4645, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "workclass", "instances": 198, "metric_value": 0.4395, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 135, "metric_value": 0.2942, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 124, "metric_value": 0.3132, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "occupation", "instances": 118, "metric_value": 0.3247, "depth": 13}
													if obj[6] == 'Exec-managerial':
														# {"feature": "sex", "instances": 43, "metric_value": 0.1594, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 30, "metric_value": 0.469, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Sales':
														# {"feature": "sex", "instances": 28, "metric_value": 0.3712, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Adm-clerical':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Tech-support':
														return '>50K'
													elif obj[6] == 'Machine-op-inspct':
														return '>50K'
													elif obj[6] == 'Craft-repair':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-inc':
											# {"feature": "occupation", "instances": 20, "metric_value": 0.2864, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 15, "metric_value": 0.3534, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 14, "metric_value": 0.3712, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 14, "metric_value": 0.3712, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Wife':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Sales':
												return '>50K'
											elif obj[6] == 'Prof-specialty':
												return '>50K'
											elif obj[6] == 'Farming-fishing':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "relationship", "instances": 18, "metric_value": 0.5033, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "occupation", "instances": 15, "metric_value": 0.5665, "depth": 12}
												if obj[6] == 'Exec-managerial':
													# {"feature": "race", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Sales':
													return '>50K'
												elif obj[6] == 'Farming-fishing':
													return '>50K'
												elif obj[6] == 'Craft-repair':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Local-gov':
											# {"feature": "occupation", "instances": 16, "metric_value": 0.896, "depth": 11}
											if obj[6] == 'Prof-specialty':
												# {"feature": "race", "instances": 10, "metric_value": 0.8813, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Adm-clerical':
												return '>50K'
											elif obj[6] == 'Protective-serv':
												return '>50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Federal-gov':
											# {"feature": "occupation", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[6] == 'Protective-serv':
												return '>50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '>50K'
											elif obj[6] == 'Exec-managerial':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'State-gov':
											# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[7] == 'Husband':
												return '>50K'
											elif obj[7] == 'Wife':
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										else: return '>50K'
									elif obj[13] == 'Philippines':
										return '>50K'
									elif obj[13] == 'China':
										return '>50K'
									elif obj[13] == 'South':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Sales':
											return '>50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'England':
										return '>50K'
									elif obj[13] == 'Peru':
										return '>50K'
									elif obj[13] == 'Puerto-Rico':
										return '>50K'
									elif obj[13] == 'Iran':
										return '<=50K'
									elif obj[13] == 'Taiwan':
										return '>50K'
									elif obj[13] == 'Germany':
										return '>50K'
									elif obj[13] == 'India':
										return '<=50K'
									elif obj[13] == 'Cuba':
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Some-college':
									# {"feature": "native-country", "instances": 147, "metric_value": 0.9717, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "race", "instances": 141, "metric_value": 0.9734, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "occupation", "instances": 133, "metric_value": 0.9701, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "workclass", "instances": 31, "metric_value": 0.9072, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 20, "metric_value": 0.8813, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 18, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "workclass", "instances": 25, "metric_value": 0.9896, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 20, "metric_value": 0.971, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 20, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "workclass", "instances": 23, "metric_value": 0.9656, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 17, "metric_value": 0.9367, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 17, "metric_value": 0.9367, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "workclass", "instances": 14, "metric_value": 0.9852, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[7] == 'Wife':
														# {"feature": "sex", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														return '<=50K'
													elif obj[7] == 'Wife':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "workclass", "instances": 10, "metric_value": 0.8813, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 9, "metric_value": 0.7642, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Wife':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "workclass", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Protective-serv':
												return '>50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Husband':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Private':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Tech-support':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Black':
											# {"feature": "occupation", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'Adm-clerical':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Wife':
													return '<=50K'
												elif obj[7] == 'Husband':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '>50K'
											elif obj[6] == 'Exec-managerial':
												return '>50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'Asian-Pac-Islander':
											return '>50K'
										elif obj[8] == 'Other':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Philippines':
										return '>50K'
									elif obj[13] == 'El-Salvador':
										return '<=50K'
									elif obj[13] == 'South':
										return '>50K'
									elif obj[13] == 'Canada':
										return '<=50K'
									elif obj[13] == 'Cuba':
										return '>50K'
									elif obj[13] == 'Mexico':
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Masters':
									# {"feature": "native-country", "instances": 107, "metric_value": 0.2302, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "relationship", "instances": 98, "metric_value": 0.1975, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "occupation", "instances": 82, "metric_value": 0.095, "depth": 11}
											if obj[6] == 'Exec-managerial':
												return '>50K'
											elif obj[6] == 'Prof-specialty':
												return '>50K'
											elif obj[6] == 'Tech-support':
												return '>50K'
											elif obj[6] == 'Sales':
												return '>50K'
											elif obj[6] == 'Craft-repair':
												return '>50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Protective-serv':
												return '>50K'
											elif obj[6] == 'Armed-Forces':
												return '>50K'
											elif obj[6] == 'Machine-op-inspct':
												return '>50K'
											else: return '>50K'
										elif obj[7] == 'Wife':
											# {"feature": "workclass", "instances": 16, "metric_value": 0.5436, "depth": 11}
											if obj[1] == 'Private':
												return '>50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "occupation", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											else: return '>50K'
										else: return '>50K'
									elif obj[13] == 'India':
										return '>50K'
									elif obj[13] == 'Philippines':
										return '>50K'
									elif obj[13] == 'China':
										return '<=50K'
									elif obj[13] == 'Germany':
										return '>50K'
									elif obj[13] == 'Greece':
										return '>50K'
									elif obj[13] == 'South':
										return '>50K'
									elif obj[13] == 'Taiwan':
										return '>50K'
									elif obj[13] == 'Japan':
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Assoc-voc':
									# {"feature": "race", "instances": 35, "metric_value": 0.9518, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "native-country", "instances": 34, "metric_value": 0.9367, "depth": 10}
										if obj[13] == 'United-States':
											# {"feature": "relationship", "instances": 33, "metric_value": 0.9457, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "workclass", "instances": 26, "metric_value": 0.9612, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "occupation", "instances": 22, "metric_value": 0.976, "depth": 13}
													if obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9911, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Exec-managerial':
														return '>50K'
													elif obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Sales':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Tech-support':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Machine-op-inspct':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Adm-clerical':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Wife':
												# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Tech-support':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											else: return '<=50K'
										elif obj[13] == 'Germany':
											return '>50K'
										else: return '>50K'
									elif obj[8] == 'Other':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == 'Assoc-acdm':
									# {"feature": "occupation", "instances": 31, "metric_value": 0.9383, "depth": 9}
									if obj[6] == 'Craft-repair':
										# {"feature": "workclass", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "native-country", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[13] == 'United-States':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[13] == 'Ireland':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Sales':
										return '>50K'
									elif obj[6] == 'Exec-managerial':
										return '>50K'
									elif obj[6] == 'Tech-support':
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										else: return '>50K'
									elif obj[6] == 'Protective-serv':
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Local-gov':
											# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[13] == 'England':
												return '<=50K'
											elif obj[13] == 'United-States':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'State-gov':
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '<=50K'
									elif obj[6] == 'Adm-clerical':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										return '>50K'
									else: return '>50K'
								elif obj[3] == '7th-8th':
									# {"feature": "workclass", "instances": 13, "metric_value": 0.7793, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'Local-gov':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Craft-repair':
											return '>50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Transport-moving':
											return '>50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Self-emp-inc':
										return '>50K'
									else: return '>50K'
								elif obj[3] == '11th':
									# {"feature": "occupation", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[6] == 'Craft-repair':
										# {"feature": "workclass", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Transport-moving':
										return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Exec-managerial':
										return '>50K'
									else: return '>50K'
								elif obj[3] == '10th':
									# {"feature": "workclass", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "occupation", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[6] == 'Craft-repair':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Sales':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Husband':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Transport-moving':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Black':
											return '>50K'
										else: return '>50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '>50K'
									else: return '>50K'
								elif obj[3] == '5th-6th':
									# {"feature": "workclass", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Exec-managerial':
											return '>50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										else: return '<=50K'
									else: return '>50K'
								elif obj[3] == '9th':
									# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1] == 'Self-emp-inc':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									elif obj[1] == 'Private':
										return '>50K'
									else: return '>50K'
								elif obj[3] == '1st-4th':
									return '<=50K'
								elif obj[3] == '12th':
									# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[13] == 'United-States':
										return '<=50K'
									elif obj[13] == 'Nicaragua':
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Preschool':
									return '<=50K'
								else: return '<=50K'
							elif float(obj[12])<=4:
								return '<=50K'
							else: return '<=50K'
						else: return '>50K'
					elif float(obj[2])<=13769:
						return '<=50K'
					else: return '<=50K'
				elif float(obj[0])<=18.88526350825298:
					return '<=50K'
				else: return '<=50K'
			elif obj[5] == 'Never-married':
				# {"feature": "hours-per-week", "instances": 10388, "metric_value": 0.1833, "depth": 4}
				if float(obj[12])<=48.94037195034036:
					# {"feature": "age", "instances": 9175, "metric_value": 0.1325, "depth": 5}
					if float(obj[0])<=37.25433337413308:
						# {"feature": "capital-loss", "instances": 7946, "metric_value": 0.0829, "depth": 6}
						if float(obj[11])<=320.6881726083144:
							# {"feature": "relationship", "instances": 7745, "metric_value": 0.077, "depth": 7}
							if obj[7] == 'Own-child':
								# {"feature": "education", "instances": 3909, "metric_value": 0.0257, "depth": 8}
								if obj[3] == 'Some-college':
									# {"feature": "workclass", "instances": 1423, "metric_value": 0.0218, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "sex", "instances": 1268, "metric_value": 0.0093, "depth": 10}
										if obj[9] == 'Female':
											return '<=50K'
										elif obj[9] == 'Male':
											# {"feature": "fnlwgt", "instances": 623, "metric_value": 0.0172, "depth": 11}
											if float(obj[2])<=208191.72231139647:
												# {"feature": "occupation", "instances": 357, "metric_value": 0.0278, "depth": 12}
												if obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Other-service':
													# {"feature": "race", "instances": 62, "metric_value": 0.1191, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 55, "metric_value": 0.1311, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														elif obj[13] == 'Canada':
															return '<=50K'
														elif obj[13] == 'Poland':
															return '<=50K'
														elif obj[13] == 'Italy':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Transport-moving':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Protective-serv':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])>208191.72231139647:
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'State-gov':
										return '<=50K'
									elif obj[1] == 'Local-gov':
										# {"feature": "occupation", "instances": 35, "metric_value": 0.316, "depth": 10}
										if obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "fnlwgt", "instances": 11, "metric_value": 0.684, "depth": 11}
											if float(obj[2])>193416:
												# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])<=193416:
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									elif obj[1] == 'Federal-gov':
										return '<=50K'
									elif obj[1] == 'Self-emp-inc':
										return '<=50K'
									elif obj[1] == 'Never-worked':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == 'HS-grad':
									return '<=50K'
								elif obj[3] == 'Bachelors':
									# {"feature": "fnlwgt", "instances": 390, "metric_value": 0.0825, "depth": 9}
									if float(obj[2])<=373931.84732527565:
										# {"feature": "occupation", "instances": 373, "metric_value": 0.0675, "depth": 10}
										if obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "sex", "instances": 78, "metric_value": 0.099, "depth": 11}
											if obj[9] == 'Female':
												# {"feature": "race", "instances": 55, "metric_value": 0.1311, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "native-country", "instances": 45, "metric_value": 0.1537, "depth": 13}
													if obj[13] == 'United-States':
														# {"feature": "workclass", "instances": 42, "metric_value": 0.1623, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'State-gov':
															return '<=50K'
														elif obj[1] == 'Self-emp-inc':
															return '<=50K'
														else: return '<=50K'
													elif obj[13] == 'El-Salvador':
														return '<=50K'
													elif obj[13] == 'Portugal':
														return '<=50K'
													elif obj[13] == 'Mexico':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Male':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Sales':
											# {"feature": "sex", "instances": 51, "metric_value": 0.1392, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "race", "instances": 28, "metric_value": 0.2223, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 24, "metric_value": 0.2499, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "native-country", "instances": 23, "metric_value": 0.258, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 11, "metric_value": 0.4395, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "native-country", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[13] == 'United-States':
													# {"feature": "race", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[13] == 'Mexico':
													return '<=50K'
												elif obj[13] == 'Canada':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[2])>373931.84732527565:
										# {"feature": "sex", "instances": 17, "metric_value": 0.3228, "depth": 10}
										if obj[9] == 'Male':
											return '<=50K'
										elif obj[9] == 'Female':
											# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									else: return '<=50K'
								elif obj[3] == '11th':
									return '<=50K'
								elif obj[3] == '10th':
									return '<=50K'
								elif obj[3] == '12th':
									return '<=50K'
								elif obj[3] == 'Assoc-acdm':
									return '<=50K'
								elif obj[3] == 'Assoc-voc':
									# {"feature": "sex", "instances": 94, "metric_value": 0.085, "depth": 9}
									if obj[9] == 'Female':
										return '<=50K'
									elif obj[9] == 'Male':
										# {"feature": "fnlwgt", "instances": 46, "metric_value": 0.1511, "depth": 10}
										if float(obj[2])<=191086.41304347827:
											# {"feature": "occupation", "instances": 28, "metric_value": 0.2223, "depth": 11}
											if obj[6] == 'Craft-repair':
												# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											else: return '<=50K'
										elif float(obj[2])>191086.41304347827:
											return '<=50K'
										else: return '<=50K'
									else: return '<=50K'
								elif obj[3] == '9th':
									return '<=50K'
								elif obj[3] == 'Masters':
									# {"feature": "fnlwgt", "instances": 35, "metric_value": 0.316, "depth": 9}
									if float(obj[2])>186741.88571428572:
										return '<=50K'
									elif float(obj[2])<=186741.88571428572:
										# {"feature": "occupation", "instances": 17, "metric_value": 0.5226, "depth": 10}
										if obj[6] == 'Prof-specialty':
											# {"feature": "workclass", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										else: return '<=50K'
									else: return '<=50K'
								elif obj[3] == '7th-8th':
									return '<=50K'
								elif obj[3] == '5th-6th':
									return '<=50K'
								elif obj[3] == 'Preschool':
									return '<=50K'
								elif obj[3] == '1st-4th':
									return '<=50K'
								else: return '<=50K'
							elif obj[7] == 'Not-in-family':
								# {"feature": "native-country", "instances": 2769, "metric_value": 0.1487, "depth": 8}
								if obj[13] == 'United-States':
									# {"feature": "education", "instances": 2529, "metric_value": 0.149, "depth": 9}
									if obj[3] == 'HS-grad':
										# {"feature": "workclass", "instances": 723, "metric_value": 0.0596, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "sex", "instances": 654, "metric_value": 0.0422, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "occupation", "instances": 370, "metric_value": 0.068, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "fnlwgt", "instances": 77, "metric_value": 0.1, "depth": 13}
													if float(obj[2])<=324004.034567071:
														return '<=50K'
													elif float(obj[2])>324004.034567071:
														# {"feature": "race", "instances": 14, "metric_value": 0.3712, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												elif obj[6] == 'Sales':
													# {"feature": "fnlwgt", "instances": 35, "metric_value": 0.1872, "depth": 13}
													if float(obj[2])<=218510.0285714286:
														return '<=50K'
													elif float(obj[2])>218510.0285714286:
														# {"feature": "race", "instances": 16, "metric_value": 0.3373, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Transport-moving':
													# {"feature": "fnlwgt", "instances": 22, "metric_value": 0.2668, "depth": 13}
													if float(obj[2])<=211710.86363636365:
														# {"feature": "race", "instances": 12, "metric_value": 0.4138, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														elif obj[8] == 'Other':
															return '<=50K'
														else: return '<=50K'
													elif float(obj[2])>211710.86363636365:
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Protective-serv':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "fnlwgt", "instances": 23, "metric_value": 0.258, "depth": 11}
											if float(obj[2])<=212712.73913043478:
												return '<=50K'
											elif float(obj[2])>212712.73913043478:
												# {"feature": "occupation", "instances": 11, "metric_value": 0.4395, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Local-gov':
											return '<=50K'
										elif obj[1] == 'Federal-gov':
											return '<=50K'
										elif obj[1] == 'State-gov':
											# {"feature": "fnlwgt", "instances": 10, "metric_value": 0.469, "depth": 11}
											if float(obj[2])>23740:
												return '<=50K'
											elif float(obj[2])<=23740:
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										else: return '<=50K'
									elif obj[3] == 'Some-college':
										# {"feature": "race", "instances": 664, "metric_value": 0.0941, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "workclass", "instances": 576, "metric_value": 0.0835, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "fnlwgt", "instances": 504, "metric_value": 0.0803, "depth": 12}
												if float(obj[2])>83243.93709702935:
													# {"feature": "occupation", "instances": 410, "metric_value": 0.095, "depth": 13}
													if obj[6] == 'Adm-clerical':
														return '<=50K'
													elif obj[6] == 'Other-service':
														# {"feature": "sex", "instances": 73, "metric_value": 0.1044, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Sales':
														# {"feature": "sex", "instances": 67, "metric_value": 0.1119, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 45, "metric_value": 0.1537, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 35, "metric_value": 0.1872, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Machine-op-inspct':
														return '<=50K'
													elif obj[6] == 'Handlers-cleaners':
														return '<=50K'
													elif obj[6] == 'Tech-support':
														# {"feature": "sex", "instances": 17, "metric_value": 0.3228, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													elif obj[6] == 'Farming-fishing':
														return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '<=50K'
													elif obj[6] == 'Priv-house-serv':
														return '<=50K'
													else: return '<=50K'
												elif float(obj[2])<=83243.93709702935:
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "sex", "instances": 13, "metric_value": 0.3912, "depth": 12}
												if obj[9] == 'Male':
													return '<=50K'
												elif obj[9] == 'Female':
													# {"feature": "fnlwgt", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if float(obj[2])>137059:
														# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[6] == 'Exec-managerial':
															return '<=50K'
														elif obj[6] == 'Adm-clerical':
															return '<=50K'
														elif obj[6] == 'Other-service':
															return '>50K'
														else: return '>50K'
													elif float(obj[2])<=137059:
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'Black':
											return '<=50K'
										elif obj[8] == 'Asian-Pac-Islander':
											# {"feature": "fnlwgt", "instances": 10, "metric_value": 0.7219, "depth": 11}
											if float(obj[2])>83374:
												# {"feature": "occupation", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Female':
														return '<=50K'
													elif obj[9] == 'Male':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])<=83374:
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Other':
											return '<=50K'
										elif obj[8] == 'Amer-Indian-Eskimo':
											return '<=50K'
										else: return '<=50K'
									elif obj[3] == 'Bachelors':
										# {"feature": "workclass", "instances": 641, "metric_value": 0.2156, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "race", "instances": 495, "metric_value": 0.2254, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "fnlwgt", "instances": 455, "metric_value": 0.2403, "depth": 12}
												if float(obj[2])<=519614.1590398431:
													# {"feature": "occupation", "instances": 452, "metric_value": 0.2415, "depth": 13}
													if obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 131, "metric_value": 0.2683, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Sales':
														# {"feature": "sex", "instances": 81, "metric_value": 0.2838, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														# {"feature": "sex", "instances": 79, "metric_value": 0.2329, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Adm-clerical':
														# {"feature": "sex", "instances": 68, "metric_value": 0.1106, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Tech-support':
														# {"feature": "sex", "instances": 36, "metric_value": 0.4138, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Machine-op-inspct':
														return '<=50K'
													elif obj[6] == 'Farming-fishing':
														return '<=50K'
													elif obj[6] == 'Handlers-cleaners':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '<=50K'
													else: return '<=50K'
												elif float(obj[2])>519614.1590398431:
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Local-gov':
											return '<=50K'
										elif obj[1] == 'State-gov':
											return '<=50K'
										elif obj[1] == 'Federal-gov':
											# {"feature": "sex", "instances": 29, "metric_value": 0.2164, "depth": 11}
											if obj[9] == 'Female':
												return '<=50K'
											elif obj[9] == 'Male':
												# {"feature": "fnlwgt", "instances": 14, "metric_value": 0.3712, "depth": 12}
												if float(obj[2])>68330:
													return '<=50K'
												elif float(obj[2])<=68330:
													# {"feature": "occupation", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[6] == 'Prof-specialty':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														elif obj[8] == 'Asian-Pac-Islander':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Tech-support':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "fnlwgt", "instances": 13, "metric_value": 0.3912, "depth": 11}
											if float(obj[2])>181485:
												return '<=50K'
											elif float(obj[2])<=181485:
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Sales':
													return '>50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												else: return '<=50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-inc':
											# {"feature": "fnlwgt", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if float(obj[2])<=306868:
												# {"feature": "occupation", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Sales':
													return '>50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])>306868:
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[3] == 'Assoc-voc':
										# {"feature": "fnlwgt", "instances": 111, "metric_value": 0.1793, "depth": 10}
										if float(obj[2])>23438:
											# {"feature": "workclass", "instances": 110, "metric_value": 0.1311, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "sex", "instances": 97, "metric_value": 0.0828, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "occupation", "instances": 52, "metric_value": 0.1371, "depth": 13}
													if obj[6] == 'Craft-repair':
														return '<=50K'
													elif obj[6] == 'Tech-support':
														return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Machine-op-inspct':
														return '<=50K'
													elif obj[6] == 'Adm-clerical':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Sales':
														return '<=50K'
													elif obj[6] == 'Handlers-cleaners':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Female':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[6] == 'Protective-serv':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Female':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											else: return '<=50K'
										elif float(obj[2])<=23438:
											return '>50K'
										else: return '>50K'
									elif obj[3] == 'Assoc-acdm':
										# {"feature": "race", "instances": 109, "metric_value": 0.1321, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "occupation", "instances": 97, "metric_value": 0.0828, "depth": 11}
											if obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[9] == 'Male':
													return '<=50K'
												elif obj[9] == 'Female':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'Black':
											# {"feature": "workclass", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Other':
											return '<=50K'
										elif obj[8] == 'Asian-Pac-Islander':
											return '<=50K'
										else: return '<=50K'
									elif obj[3] == 'Masters':
										# {"feature": "fnlwgt", "instances": 102, "metric_value": 0.5226, "depth": 10}
										if float(obj[2])>33975:
											# {"feature": "workclass", "instances": 101, "metric_value": 0.4966, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 62, "metric_value": 0.6744, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 32, "metric_value": 0.6253, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 28, "metric_value": 0.6769, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "race", "instances": 19, "metric_value": 0.8997, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 16, "metric_value": 0.896, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Priv-house-serv':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											else: return '<=50K'
										elif float(obj[2])<=33975:
											return '>50K'
										else: return '>50K'
									elif obj[3] == '11th':
										# {"feature": "fnlwgt", "instances": 64, "metric_value": 0.1161, "depth": 10}
										if float(obj[2])<=401561.22551564465:
											return '<=50K'
										elif float(obj[2])>401561.22551564465:
											# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[3] == '10th':
										return '<=50K'
									elif obj[3] == '12th':
										return '<=50K'
									elif obj[3] == '9th':
										# {"feature": "fnlwgt", "instances": 19, "metric_value": 0.2975, "depth": 10}
										if float(obj[2])>111567:
											return '<=50K'
										elif float(obj[2])<=111567:
											# {"feature": "occupation", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[6] == 'Sales':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[3] == '7th-8th':
										return '<=50K'
									elif obj[3] == '5th-6th':
										return '<=50K'
									elif obj[3] == '1st-4th':
										return '<=50K'
									elif obj[3] == 'Preschool':
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'Mexico':
									# {"feature": "occupation", "instances": 64, "metric_value": 0.1161, "depth": 9}
									if obj[6] == 'Craft-repair':
										return '<=50K'
									elif obj[6] == 'Farming-fishing':
										# {"feature": "education", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[3] == 'Preschool':
											return '<=50K'
										elif obj[3] == '5th-6th':
											return '<=50K'
										elif obj[3] == '1st-4th':
											return '<=50K'
										elif obj[3] == 'HS-grad':
											return '<=50K'
										elif obj[3] == '7th-8th':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Priv-house-serv':
										return '<=50K'
									elif obj[6] == 'Sales':
										return '<=50K'
									elif obj[6] == 'Transport-moving':
										return '<=50K'
									elif obj[6] == 'Adm-clerical':
										return '<=50K'
									elif obj[6] == 'Exec-managerial':
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'Jamaica':
									return '<=50K'
								elif obj[13] == 'Philippines':
									# {"feature": "fnlwgt", "instances": 14, "metric_value": 0.3712, "depth": 9}
									if float(obj[2])>66297:
										return '<=50K'
									elif float(obj[2])<=66297:
										return '>50K'
									else: return '>50K'
								elif obj[13] == 'Germany':
									return '<=50K'
								elif obj[13] == 'Canada':
									return '<=50K'
								elif obj[13] == 'El-Salvador':
									return '<=50K'
								elif obj[13] == 'England':
									# {"feature": "fnlwgt", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if float(obj[2])<=253799:
										return '<=50K'
									elif float(obj[2])>253799:
										# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3] == 'Some-college':
											return '>50K'
										elif obj[3] == 'HS-grad':
											return '<=50K'
										else: return '<=50K'
									else: return '>50K'
								elif obj[13] == 'Guatemala':
									return '<=50K'
								elif obj[13] == 'Ireland':
									return '<=50K'
								elif obj[13] == 'Japan':
									return '<=50K'
								elif obj[13] == 'Puerto-Rico':
									return '<=50K'
								elif obj[13] == 'Columbia':
									return '<=50K'
								elif obj[13] == 'Vietnam':
									return '<=50K'
								elif obj[13] == 'India':
									return '<=50K'
								elif obj[13] == 'South':
									return '<=50K'
								elif obj[13] == 'Taiwan':
									# {"feature": "fnlwgt", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if float(obj[2])<=172152:
										return '<=50K'
									elif float(obj[2])>172152:
										return '>50K'
									else: return '>50K'
								elif obj[13] == 'Thailand':
									return '<=50K'
								elif obj[13] == 'France':
									# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'Self-emp-inc':
										return '>50K'
									else: return '>50K'
								elif obj[13] == 'Dominican-Republic':
									return '<=50K'
								elif obj[13] == 'Italy':
									return '<=50K'
								elif obj[13] == 'Hong':
									return '<=50K'
								elif obj[13] == 'Cuba':
									return '<=50K'
								elif obj[13] == 'Poland':
									return '<=50K'
								elif obj[13] == 'China':
									return '<=50K'
								elif obj[13] == 'Laos':
									return '<=50K'
								elif obj[13] == 'Cambodia':
									return '<=50K'
								elif obj[13] == 'Honduras':
									return '<=50K'
								elif obj[13] == 'Ecuador':
									return '<=50K'
								elif obj[13] == 'Trinadad&Tobago':
									return '<=50K'
								elif obj[13] == 'Hungary':
									return '<=50K'
								elif obj[13] == 'Greece':
									return '<=50K'
								elif obj[13] == 'Peru':
									return '<=50K'
								elif obj[13] == 'Iran':
									return '<=50K'
								elif obj[13] == 'Scotland':
									return '<=50K'
								elif obj[13] == 'Nicaragua':
									return '<=50K'
								elif obj[13] == 'Outlying-US(Guam-USVI-etc)':
									return '<=50K'
								elif obj[13] == 'Portugal':
									return '<=50K'
								elif obj[13] == 'Yugoslavia':
									return '<=50K'
								else: return '<=50K'
							elif obj[7] == 'Unmarried':
								# {"feature": "education", "instances": 596, "metric_value": 0.0457, "depth": 8}
								if obj[3] == 'HS-grad':
									return '<=50K'
								elif obj[3] == 'Some-college':
									return '<=50K'
								elif obj[3] == 'Bachelors':
									# {"feature": "race", "instances": 47, "metric_value": 0.3425, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "occupation", "instances": 24, "metric_value": 0.5436, "depth": 10}
										if obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "fnlwgt", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if float(obj[2])>145964:
												# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[9] == 'Female':
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Male':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])<=145964:
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Sales':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										else: return '<=50K'
									elif obj[8] == 'Black':
										return '<=50K'
									elif obj[8] == 'Asian-Pac-Islander':
										return '<=50K'
									elif obj[8] == 'Other':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == '11th':
									return '<=50K'
								elif obj[3] == 'Assoc-voc':
									return '<=50K'
								elif obj[3] == '10th':
									return '<=50K'
								elif obj[3] == 'Assoc-acdm':
									return '<=50K'
								elif obj[3] == '7th-8th':
									return '<=50K'
								elif obj[3] == '9th':
									return '<=50K'
								elif obj[3] == '12th':
									return '<=50K'
								elif obj[3] == '5th-6th':
									return '<=50K'
								elif obj[3] == 'Masters':
									return '<=50K'
								elif obj[3] == '1st-4th':
									return '<=50K'
								else: return '<=50K'
							elif obj[7] == 'Other-relative':
								# {"feature": "workclass", "instances": 471, "metric_value": 0.0219, "depth": 8}
								if obj[1] == 'Private':
									return '<=50K'
								elif obj[1] == 'Local-gov':
									# {"feature": "native-country", "instances": 12, "metric_value": 0.4138, "depth": 9}
									if obj[13] == 'United-States':
										return '<=50K'
									elif obj[13] == 'Haiti':
										return '<=50K'
									elif obj[13] == 'Guatemala':
										return '>50K'
									else: return '>50K'
								elif obj[1] == 'Federal-gov':
									return '<=50K'
								elif obj[1] == 'Self-emp-not-inc':
									return '<=50K'
								elif obj[1] == 'State-gov':
									return '<=50K'
								elif obj[1] == 'Self-emp-inc':
									return '<=50K'
								else: return '<=50K'
							else: return '<=50K'
						elif float(obj[11])>320.6881726083144:
							# {"feature": "education", "instances": 201, "metric_value": 0.2638, "depth": 7}
							if obj[3] == 'HS-grad':
								return '<=50K'
							elif obj[3] == 'Some-college':
								# {"feature": "fnlwgt", "instances": 58, "metric_value": 0.1257, "depth": 8}
								if float(obj[2])>92807.35149600428:
									return '<=50K'
								elif float(obj[2])<=92807.35149600428:
									# {"feature": "workclass", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'Local-gov':
										return '>50K'
									elif obj[1] == 'State-gov':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									else: return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Bachelors':
								# {"feature": "workclass", "instances": 39, "metric_value": 0.6194, "depth": 8}
								if obj[1] == 'Private':
									# {"feature": "occupation", "instances": 35, "metric_value": 0.5917, "depth": 9}
									if obj[6] == 'Exec-managerial':
										# {"feature": "relationship", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[7] == 'Not-in-family':
											# {"feature": "fnlwgt", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if float(obj[2])>82246:
												# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "race", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Female':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif float(obj[2])<=82246:
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Own-child':
											return '<=50K'
										elif obj[7] == 'Other-relative':
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Sales':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										# {"feature": "relationship", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[7] == 'Not-in-family':
											return '<=50K'
										elif obj[7] == 'Own-child':
											# {"feature": "fnlwgt", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if float(obj[2])>77071:
												return '>50K'
											elif float(obj[2])<=77071:
												return '<=50K'
											else: return '<=50K'
										else: return '>50K'
									elif obj[6] == 'Tech-support':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Craft-repair':
										return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Adm-clerical':
										return '<=50K'
									elif obj[6] == 'Other-service':
										return '<=50K'
									else: return '<=50K'
								elif obj[1] == 'Federal-gov':
									return '<=50K'
								elif obj[1] == 'Self-emp-not-inc':
									return '>50K'
								elif obj[1] == 'Local-gov':
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == '11th':
								return '<=50K'
							elif obj[3] == '10th':
								return '<=50K'
							elif obj[3] == 'Assoc-acdm':
								# {"feature": "race", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[8] == 'White':
									return '<=50K'
								elif obj[8] == 'Black':
									return '>50K'
								else: return '>50K'
							elif obj[3] == 'Masters':
								# {"feature": "occupation", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[6] == 'Prof-specialty':
									return '<=50K'
								elif obj[6] == 'Exec-managerial':
									return '>50K'
								else: return '>50K'
							elif obj[3] == 'Assoc-voc':
								return '<=50K'
							elif obj[3] == '12th':
								return '<=50K'
							elif obj[3] == '9th':
								return '<=50K'
							elif obj[3] == '7th-8th':
								return '<=50K'
							else: return '<=50K'
						else: return '<=50K'
					elif float(obj[0])>37.25433337413308:
						# {"feature": "capital-loss", "instances": 1229, "metric_value": 0.3689, "depth": 6}
						if float(obj[11])<=1229.4951694610174:
							# {"feature": "native-country", "instances": 1176, "metric_value": 0.3455, "depth": 7}
							if obj[13] == 'United-States':
								# {"feature": "education", "instances": 1084, "metric_value": 0.3594, "depth": 8}
								if obj[3] == 'HS-grad':
									# {"feature": "occupation", "instances": 373, "metric_value": 0.1189, "depth": 9}
									if obj[6] == 'Adm-clerical':
										# {"feature": "fnlwgt", "instances": 90, "metric_value": 0.1537, "depth": 10}
										if float(obj[2])<=183301.35555555555:
											return '<=50K'
										elif float(obj[2])>183301.35555555555:
											# {"feature": "relationship", "instances": 42, "metric_value": 0.2762, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "workclass", "instances": 18, "metric_value": 0.3095, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Unmarried':
												return '<=50K'
											elif obj[7] == 'Own-child':
												# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[9] == 'Male':
													return '<=50K'
												elif obj[9] == 'Female':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1] == 'Private':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Craft-repair':
										# {"feature": "fnlwgt", "instances": 47, "metric_value": 0.1485, "depth": 10}
										if float(obj[2])>95184.8961497635:
											return '<=50K'
										elif float(obj[2])<=95184.8961497635:
											# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Sales':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Exec-managerial':
										# {"feature": "fnlwgt", "instances": 27, "metric_value": 0.2285, "depth": 10}
										if float(obj[2])<=281106.3143830763:
											return '<=50K'
										elif float(obj[2])>281106.3143830763:
											# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[9] == 'Female':
												return '<=50K'
											elif obj[9] == 'Male':
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										# {"feature": "fnlwgt", "instances": 20, "metric_value": 0.2864, "depth": 10}
										if float(obj[2])>112497:
											return '<=50K'
										elif float(obj[2])<=112497:
											# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == 'Female':
													return '<=50K'
												elif obj[9] == 'Male':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Transport-moving':
										return '<=50K'
									elif obj[6] == 'Farming-fishing':
										return '<=50K'
									elif obj[6] == 'Tech-support':
										return '<=50K'
									elif obj[6] == 'Protective-serv':
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Local-gov':
											return '<=50K'
										elif obj[1] == 'State-gov':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Priv-house-serv':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == 'Some-college':
									# {"feature": "fnlwgt", "instances": 215, "metric_value": 0.2913, "depth": 9}
									if float(obj[2])>83135.23869857001:
										# {"feature": "occupation", "instances": 187, "metric_value": 0.3228, "depth": 10}
										if obj[6] == 'Adm-clerical':
											# {"feature": "race", "instances": 51, "metric_value": 0.2387, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "relationship", "instances": 38, "metric_value": 0.2975, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "sex", "instances": 22, "metric_value": 0.2668, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "workclass", "instances": 16, "metric_value": 0.3373, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'State-gov':
															return '<=50K'
														elif obj[1] == 'Local-gov':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												elif obj[7] == 'Unmarried':
													# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[1] == 'Private':
															return '>50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '<=50K'
														elif obj[1] == 'Federal-gov':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Craft-repair':
											# {"feature": "relationship", "instances": 25, "metric_value": 0.4022, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "workclass", "instances": 16, "metric_value": 0.3373, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											elif obj[7] == 'Unmarried':
												# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											# {"feature": "sex", "instances": 20, "metric_value": 0.6098, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "race", "instances": 12, "metric_value": 0.8113, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "workclass", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '<=50K'
														elif obj[1] == 'State-gov':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '>50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "relationship", "instances": 17, "metric_value": 0.5226, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "workclass", "instances": 13, "metric_value": 0.6194, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Unmarried':
												return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[9] == 'Male':
												return '<=50K'
											elif obj[9] == 'Female':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Unmarried':
													return '<=50K'
												elif obj[7] == 'Not-in-family':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Local-gov':
												# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == 'Male':
													return '<=50K'
												elif obj[9] == 'Female':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Priv-house-serv':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[2])<=83135.23869857001:
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == 'Bachelors':
									# {"feature": "fnlwgt", "instances": 185, "metric_value": 0.6521, "depth": 9}
									if float(obj[2])<=361448.97064698895:
										# {"feature": "occupation", "instances": 177, "metric_value": 0.6693, "depth": 10}
										if obj[6] == 'Prof-specialty':
											# {"feature": "race", "instances": 66, "metric_value": 0.799, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "sex", "instances": 58, "metric_value": 0.8247, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "workclass", "instances": 30, "metric_value": 0.9481, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "relationship", "instances": 21, "metric_value": 0.9852, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7] == 'Own-child':
															return '>50K'
														elif obj[7] == 'Not-in-family':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Female':
													# {"feature": "workclass", "instances": 28, "metric_value": 0.5917, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "relationship", "instances": 16, "metric_value": 0.5436, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '>50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Not-in-family':
													return '<=50K'
												elif obj[7] == 'Unmarried':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "sex", "instances": 36, "metric_value": 0.65, "depth": 11}
											if obj[9] == 'Female':
												# {"feature": "workclass", "instances": 20, "metric_value": 0.2864, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 14, "metric_value": 0.3712, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 11, "metric_value": 0.4395, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Male':
												# {"feature": "workclass", "instances": 16, "metric_value": 0.896, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "race", "instances": 25, "metric_value": 0.4022, "depth": 11}
											if obj[8] == 'White':
												return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											# {"feature": "race", "instances": 18, "metric_value": 0.7642, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 17, "metric_value": 0.6723, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "relationship", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Other-service':
											# {"feature": "sex", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "workclass", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Female':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Priv-house-serv':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '>50K'
										else: return '>50K'
									elif float(obj[2])>361448.97064698895:
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == 'Masters':
									# {"feature": "race", "instances": 106, "metric_value": 0.6987, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "relationship", "instances": 100, "metric_value": 0.7015, "depth": 10}
										if obj[7] == 'Not-in-family':
											# {"feature": "fnlwgt", "instances": 87, "metric_value": 0.7572, "depth": 11}
											if float(obj[2])<=336095.4394288431:
												# {"feature": "occupation", "instances": 84, "metric_value": 0.7713, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "workclass", "instances": 54, "metric_value": 0.7963, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 24, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 18, "metric_value": 0.8524, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "workclass", "instances": 14, "metric_value": 0.7496, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "workclass", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														return '>50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Protective-serv':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])>336095.4394288431:
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Own-child':
											return '<=50K'
										elif obj[7] == 'Unmarried':
											return '<=50K'
										elif obj[7] == 'Other-relative':
											return '<=50K'
										else: return '<=50K'
									elif obj[8] == 'Black':
										return '<=50K'
									elif obj[8] == 'Asian-Pac-Islander':
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Assoc-voc':
									# {"feature": "workclass", "instances": 40, "metric_value": 0.2864, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "fnlwgt", "instances": 31, "metric_value": 0.2056, "depth": 10}
										if float(obj[2])<=263623.78105238365:
											return '<=50K'
										elif float(obj[2])>263623.78105238365:
											# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[1] == 'Local-gov':
										return '<=50K'
									elif obj[1] == 'State-gov':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '>50K'
									elif obj[1] == 'Federal-gov':
										return '<=50K'
									elif obj[1] == 'Self-emp-inc':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == 'Assoc-acdm':
									# {"feature": "workclass", "instances": 38, "metric_value": 0.2975, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'Local-gov':
										# {"feature": "fnlwgt", "instances": 6, "metric_value": 0.65, "depth": 10}
										if float(obj[2])>183765:
											return '<=50K'
										elif float(obj[2])<=183765:
											return '>50K'
										else: return '>50K'
									elif obj[1] == 'Federal-gov':
										# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '>50K'
										else: return '>50K'
									elif obj[1] == 'Self-emp-inc':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == '11th':
									return '<=50K'
								elif obj[3] == '7th-8th':
									# {"feature": "fnlwgt", "instances": 26, "metric_value": 0.2352, "depth": 9}
									if float(obj[2])>44990.34050901054:
										return '<=50K'
									elif float(obj[2])<=44990.34050901054:
										# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '>50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										else: return '<=50K'
									else: return '<=50K'
								elif obj[3] == '10th':
									# {"feature": "fnlwgt", "instances": 23, "metric_value": 0.258, "depth": 9}
									if float(obj[2])<=216999.52664202108:
										return '<=50K'
									elif float(obj[2])>216999.52664202108:
										# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[7] == 'Not-in-family':
											return '<=50K'
										elif obj[7] == 'Unmarried':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif obj[3] == '9th':
									return '<=50K'
								elif obj[3] == '12th':
									return '<=50K'
								elif obj[3] == '5th-6th':
									return '<=50K'
								elif obj[3] == 'Preschool':
									return '<=50K'
								elif obj[3] == '1st-4th':
									return '<=50K'
								else: return '<=50K'
							elif obj[13] == 'Mexico':
								return '<=50K'
							elif obj[13] == 'Dominican-Republic':
								return '<=50K'
							elif obj[13] == 'Canada':
								return '<=50K'
							elif obj[13] == 'Puerto-Rico':
								return '<=50K'
							elif obj[13] == 'Philippines':
								return '<=50K'
							elif obj[13] == 'Cuba':
								return '<=50K'
							elif obj[13] == 'El-Salvador':
								return '<=50K'
							elif obj[13] == 'Peru':
								return '<=50K'
							elif obj[13] == 'Columbia':
								return '<=50K'
							elif obj[13] == 'Poland':
								return '<=50K'
							elif obj[13] == 'Haiti':
								return '<=50K'
							elif obj[13] == 'Jamaica':
								return '<=50K'
							elif obj[13] == 'Portugal':
								return '<=50K'
							elif obj[13] == 'Germany':
								return '<=50K'
							elif obj[13] == 'Vietnam':
								return '<=50K'
							elif obj[13] == 'Laos':
								return '<=50K'
							elif obj[13] == 'Outlying-US(Guam-USVI-etc)':
								return '<=50K'
							elif obj[13] == 'Ireland':
								# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 8}
								if float(obj[2])<=120277:
									return '<=50K'
								elif float(obj[2])>120277:
									return '>50K'
								else: return '>50K'
							elif obj[13] == 'Thailand':
								return '<=50K'
							elif obj[13] == 'Cambodia':
								return '<=50K'
							elif obj[13] == 'England':
								return '<=50K'
							elif obj[13] == 'Hungary':
								return '<=50K'
							elif obj[13] == 'India':
								return '<=50K'
							elif obj[13] == 'Ecuador':
								return '<=50K'
							elif obj[13] == 'Nicaragua':
								return '<=50K'
							elif obj[13] == 'Japan':
								return '>50K'
							elif obj[13] == 'South':
								return '<=50K'
							elif obj[13] == 'China':
								return '<=50K'
							elif obj[13] == 'Iran':
								return '<=50K'
							elif obj[13] == 'Greece':
								return '<=50K'
							elif obj[13] == 'Trinadad&Tobago':
								return '<=50K'
							else: return '<=50K'
						elif float(obj[11])>1229.4951694610174:
							# {"feature": "fnlwgt", "instances": 53, "metric_value": 0.7368, "depth": 7}
							if float(obj[2])<=285232.7749988043:
								# {"feature": "occupation", "instances": 44, "metric_value": 0.8113, "depth": 8}
								if obj[6] == 'Prof-specialty':
									# {"feature": "education", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[3] == 'Masters':
										return '<=50K'
									elif obj[3] == 'Some-college':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Local-gov':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										else: return '>50K'
									elif obj[3] == 'HS-grad':
										return '<=50K'
									elif obj[3] == 'Assoc-voc':
										return '>50K'
									elif obj[3] == 'Bachelors':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Adm-clerical':
									return '<=50K'
								elif obj[6] == 'Sales':
									# {"feature": "workclass", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[9] == 'Male':
											# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == 'Bachelors':
												return '<=50K'
											elif obj[3] == 'Masters':
												return '>50K'
											elif obj[3] == 'HS-grad':
												return '>50K'
											else: return '>50K'
										elif obj[9] == 'Female':
											return '>50K'
										else: return '>50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Other-service':
									return '<=50K'
								elif obj[6] == 'Exec-managerial':
									# {"feature": "education", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[3] == 'Bachelors':
										return '<=50K'
									elif obj[3] == 'Masters':
										return '<=50K'
									elif obj[3] == 'Some-college':
										return '>50K'
									elif obj[3] == '11th':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Handlers-cleaners':
									return '<=50K'
								elif obj[6] == 'Tech-support':
									return '<=50K'
								elif obj[6] == 'Craft-repair':
									# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == 'HS-grad':
										return '>50K'
									elif obj[3] == 'Some-college':
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Protective-serv':
									return '>50K'
								elif obj[6] == 'Transport-moving':
									return '<=50K'
								elif obj[6] == 'Machine-op-inspct':
									return '<=50K'
								else: return '<=50K'
							elif float(obj[2])>285232.7749988043:
								return '<=50K'
							else: return '<=50K'
						else: return '<=50K'
					else: return '<=50K'
				elif float(obj[12])>48.94037195034036:
					# {"feature": "capital-loss", "instances": 1213, "metric_value": 0.4656, "depth": 5}
					if float(obj[11])<=2339:
						# {"feature": "relationship", "instances": 1208, "metric_value": 0.4536, "depth": 6}
						if obj[7] == 'Not-in-family':
							# {"feature": "age", "instances": 803, "metric_value": 0.5663, "depth": 7}
							if float(obj[0])>22.655650480794634:
								# {"feature": "native-country", "instances": 729, "metric_value": 0.5947, "depth": 8}
								if obj[13] == 'United-States':
									# {"feature": "fnlwgt", "instances": 678, "metric_value": 0.6109, "depth": 9}
									if float(obj[2])>23157:
										# {"feature": "education", "instances": 677, "metric_value": 0.6115, "depth": 10}
										if obj[3] == 'Bachelors':
											# {"feature": "race", "instances": 235, "metric_value": 0.785, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "workclass", "instances": 210, "metric_value": 0.7584, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "occupation", "instances": 147, "metric_value": 0.7919, "depth": 13}
													if obj[6] == 'Exec-managerial':
														# {"feature": "sex", "instances": 48, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 38, "metric_value": 0.6292, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Sales':
														# {"feature": "sex", "instances": 32, "metric_value": 0.896, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Adm-clerical':
														# {"feature": "sex", "instances": 13, "metric_value": 0.3912, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Tech-support':
														# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Craft-repair':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													elif obj[6] == 'Machine-op-inspct':
														return '<=50K'
													elif obj[6] == 'Farming-fishing':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "occupation", "instances": 22, "metric_value": 0.5746, "depth": 13}
													if obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 17, "metric_value": 0.6723, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Tech-support':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "occupation", "instances": 15, "metric_value": 0.8366, "depth": 13}
													if obj[6] == 'Sales':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '>50K'
													elif obj[6] == 'Craft-repair':
														return '<=50K'
													elif obj[6] == 'Farming-fishing':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "sex", "instances": 9, "metric_value": 0.7642, "depth": 13}
													if obj[9] == 'Male':
														return '<=50K'
													elif obj[9] == 'Female':
														# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[6] == 'Sales':
															return '<=50K'
														elif obj[6] == 'Prof-specialty':
															return '>50K'
														elif obj[6] == 'Exec-managerial':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Federal-gov':
													# {"feature": "occupation", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Protective-serv':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Tech-support':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Adm-clerical':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "sex", "instances": 16, "metric_value": 0.9887, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "occupation", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[6] == 'Prof-specialty':
														return '>50K'
													elif obj[6] == 'Exec-managerial':
														# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1] == 'Private':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Tech-support':
														return '>50K'
													elif obj[6] == 'Craft-repair':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													elif obj[6] == 'Sales':
														return '>50K'
													else: return '>50K'
												elif obj[9] == 'Female':
													# {"feature": "occupation", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Sales':
														return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '>50K'
													elif obj[6] == 'Adm-clerical':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Other':
												# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Sales':
													return '>50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[6] == 'Sales':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											else: return '<=50K'
										elif obj[3] == 'HS-grad':
											# {"feature": "race", "instances": 157, "metric_value": 0.3419, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 144, "metric_value": 0.3638, "depth": 12}
												if obj[6] == 'Craft-repair':
													# {"feature": "workclass", "instances": 26, "metric_value": 0.6194, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 21, "metric_value": 0.4537, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Transport-moving':
													return '<=50K'
												elif obj[6] == 'Sales':
													# {"feature": "sex", "instances": 17, "metric_value": 0.5226, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "workclass", "instances": 13, "metric_value": 0.6194, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'Self-emp-inc':
															return '<=50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "workclass", "instances": 16, "metric_value": 0.3373, "depth": 13}
													if obj[1] == 'Private':
														return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Farming-fishing':
													# {"feature": "workclass", "instances": 15, "metric_value": 0.3534, "depth": 13}
													if obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Private':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													# {"feature": "sex", "instances": 14, "metric_value": 0.3712, "depth": 13}
													if obj[9] == 'Male':
														return '<=50K'
													elif obj[9] == 'Female':
														# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '<=50K'
														elif obj[1] == 'Self-emp-inc':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												elif obj[6] == 'Priv-house-serv':
													return '<=50K'
												elif obj[6] == 'Protective-serv':
													return '<=50K'
												elif obj[6] == 'Armed-Forces':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											elif obj[8] == 'Other':
												return '<=50K'
											else: return '<=50K'
										elif obj[3] == 'Some-college':
											# {"feature": "race", "instances": 124, "metric_value": 0.3755, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 113, "metric_value": 0.4009, "depth": 12}
												if obj[6] == 'Sales':
													# {"feature": "workclass", "instances": 25, "metric_value": 0.4022, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 18, "metric_value": 0.5033, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "workclass", "instances": 24, "metric_value": 0.5436, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 18, "metric_value": 0.3095, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "sex", "instances": 20, "metric_value": 0.2864, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "workclass", "instances": 16, "metric_value": 0.3373, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'Federal-gov':
															return '<=50K'
														elif obj[1] == 'State-gov':
															return '<=50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Transport-moving':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[9] == 'Male':
														return '<=50K'
													elif obj[9] == 'Female':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Protective-serv':
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Private':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											elif obj[8] == 'Other':
												return '<=50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											else: return '<=50K'
										elif obj[3] == 'Masters':
											# {"feature": "sex", "instances": 72, "metric_value": 0.8113, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "occupation", "instances": 46, "metric_value": 0.9109, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 28, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "workclass", "instances": 27, "metric_value": 0.8256, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'Local-gov':
															return '<=50K'
														elif obj[1] == 'State-gov':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													# {"feature": "workclass", "instances": 8, "metric_value": 0.9544, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "workclass", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'Black':
															return '>50K'
														elif obj[8] == 'White':
															return '>50K'
														elif obj[8] == 'Asian-Pac-Islander':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Adm-clerical':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'State-gov':
														return '>50K'
													elif obj[1] == 'Private':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '>50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												# {"feature": "workclass", "instances": 26, "metric_value": 0.5159, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "occupation", "instances": 12, "metric_value": 0.8113, "depth": 13}
													if obj[6] == 'Prof-specialty':
														# {"feature": "race", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Craft-repair':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[3] == 'Assoc-voc':
											# {"feature": "race", "instances": 29, "metric_value": 0.4798, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "occupation", "instances": 28, "metric_value": 0.3712, "depth": 12}
												if obj[6] == 'Protective-serv':
													# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Private':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Sales':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Transport-moving':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													return '>50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '>50K'
											else: return '>50K'
										elif obj[3] == 'Assoc-acdm':
											# {"feature": "occupation", "instances": 28, "metric_value": 0.6769, "depth": 11}
											if obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[9] == 'Female':
													return '<=50K'
												elif obj[9] == 'Male':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Private':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Priv-house-serv':
												return '<=50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											else: return '<=50K'
										elif obj[3] == '11th':
											# {"feature": "occupation", "instances": 10, "metric_value": 0.469, "depth": 11}
											if obj[6] == 'Transport-moving':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Priv-house-serv':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											else: return '<=50K'
										elif obj[3] == '12th':
											return '<=50K'
										elif obj[3] == '10th':
											return '<=50K'
										elif obj[3] == '9th':
											# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == 'Craft-repair':
												return '>50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											else: return '<=50K'
										elif obj[3] == '7th-8th':
											return '<=50K'
										elif obj[3] == '5th-6th':
											return '<=50K'
										elif obj[3] == '1st-4th':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[2])<=23157:
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'Mexico':
									# {"feature": "education", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[3] == '1st-4th':
										return '<=50K'
									elif obj[3] == '5th-6th':
										return '<=50K'
									elif obj[3] == 'Bachelors':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Private':
											return '>50K'
										else: return '>50K'
									elif obj[3] == '10th':
										return '<=50K'
									elif obj[3] == 'HS-grad':
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'England':
									# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6] == 'Tech-support':
										return '<=50K'
									elif obj[6] == 'Priv-house-serv':
										return '<=50K'
									elif obj[6] == 'Exec-managerial':
										return '>50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'Dominican-Republic':
									return '<=50K'
								elif obj[13] == 'Iran':
									return '<=50K'
								elif obj[13] == 'Hungary':
									return '<=50K'
								elif obj[13] == 'Cuba':
									return '<=50K'
								elif obj[13] == 'France':
									return '<=50K'
								elif obj[13] == 'Jamaica':
									return '<=50K'
								elif obj[13] == 'Outlying-US(Guam-USVI-etc)':
									return '<=50K'
								elif obj[13] == 'El-Salvador':
									return '<=50K'
								elif obj[13] == 'Taiwan':
									return '<=50K'
								elif obj[13] == 'Germany':
									return '<=50K'
								elif obj[13] == 'Columbia':
									return '<=50K'
								elif obj[13] == 'Ecuador':
									return '<=50K'
								elif obj[13] == 'South':
									return '<=50K'
								elif obj[13] == 'Scotland':
									return '<=50K'
								elif obj[13] == 'Guatemala':
									return '<=50K'
								elif obj[13] == 'China':
									return '<=50K'
								elif obj[13] == 'Haiti':
									return '<=50K'
								elif obj[13] == 'Poland':
									return '<=50K'
								elif obj[13] == 'Puerto-Rico':
									return '<=50K'
								elif obj[13] == 'Canada':
									return '<=50K'
								elif obj[13] == 'Trinadad&Tobago':
									return '<=50K'
								elif obj[13] == 'Italy':
									return '>50K'
								elif obj[13] == 'Philippines':
									return '<=50K'
								elif obj[13] == 'Japan':
									return '<=50K'
								elif obj[13] == 'Ireland':
									return '<=50K'
								else: return '<=50K'
							elif float(obj[0])<=22.655650480794634:
								# {"feature": "workclass", "instances": 74, "metric_value": 0.1793, "depth": 8}
								if obj[1] == 'Private':
									# {"feature": "education", "instances": 69, "metric_value": 0.1093, "depth": 9}
									if obj[3] == 'HS-grad':
										return '<=50K'
									elif obj[3] == 'Some-college':
										return '<=50K'
									elif obj[3] == '11th':
										return '<=50K'
									elif obj[3] == 'Bachelors':
										return '<=50K'
									elif obj[3] == 'Assoc-acdm':
										return '<=50K'
									elif obj[3] == 'Preschool':
										return '<=50K'
									elif obj[3] == '10th':
										return '<=50K'
									elif obj[3] == '12th':
										return '<=50K'
									elif obj[3] == '5th-6th':
										return '<=50K'
									elif obj[3] == '7th-8th':
										return '>50K'
									elif obj[3] == 'Assoc-voc':
										return '<=50K'
									elif obj[3] == '9th':
										return '<=50K'
									elif obj[3] == '1st-4th':
										return '<=50K'
									else: return '<=50K'
								elif obj[1] == 'State-gov':
									# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 9}
									if float(obj[2])>39236:
										return '>50K'
									elif float(obj[2])<=39236:
										return '<=50K'
									else: return '<=50K'
								elif obj[1] == 'Self-emp-not-inc':
									return '<=50K'
								elif obj[1] == 'Local-gov':
									return '<=50K'
								else: return '<=50K'
							else: return '<=50K'
						elif obj[7] == 'Own-child':
							# {"feature": "race", "instances": 269, "metric_value": 0.0883, "depth": 7}
							if obj[8] == 'White':
								# {"feature": "fnlwgt", "instances": 233, "metric_value": 0.0399, "depth": 8}
								if float(obj[2])>68401.56437596183:
									return '<=50K'
								elif float(obj[2])<=68401.56437596183:
									# {"feature": "age", "instances": 39, "metric_value": 0.172, "depth": 9}
									if float(obj[0])<=27:
										return '<=50K'
									elif float(obj[0])>27:
										# {"feature": "occupation", "instances": 11, "metric_value": 0.4395, "depth": 10}
										if obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '>50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										else: return '<=50K'
									else: return '<=50K'
								else: return '<=50K'
							elif obj[8] == 'Black':
								return '<=50K'
							elif obj[8] == 'Asian-Pac-Islander':
								# {"feature": "fnlwgt", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if float(obj[2])>153078:
									return '<=50K'
								elif float(obj[2])<=153078:
									# {"feature": "native-country", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3] == 'HS-grad':
											# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if float(obj[0])>26:
												return '<=50K'
											elif float(obj[0])<=26:
												return '>50K'
											else: return '>50K'
										elif obj[3] == 'Bachelors':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Philippines':
										return '>50K'
									else: return '>50K'
								else: return '<=50K'
							elif obj[8] == 'Other':
								return '<=50K'
							elif obj[8] == 'Amer-Indian-Eskimo':
								return '<=50K'
							else: return '<=50K'
						elif obj[7] == 'Unmarried':
							# {"feature": "age", "instances": 81, "metric_value": 0.2838, "depth": 7}
							if float(obj[0])<=47.958340765792954:
								# {"feature": "fnlwgt", "instances": 79, "metric_value": 0.1703, "depth": 8}
								if float(obj[2])<=190026.46835443037:
									return '<=50K'
								elif float(obj[2])>190026.46835443037:
									# {"feature": "occupation", "instances": 32, "metric_value": 0.3373, "depth": 9}
									if obj[6] == 'Sales':
										# {"feature": "education", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[3] == 'Some-college':
											return '<=50K'
										elif obj[3] == 'HS-grad':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Private':
												return '>50K'
											else: return '>50K'
										elif obj[3] == 'Bachelors':
											return '<=50K'
										elif obj[3] == 'Masters':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Exec-managerial':
										return '<=50K'
									elif obj[6] == 'Craft-repair':
										return '<=50K'
									elif obj[6] == 'Farming-fishing':
										return '<=50K'
									elif obj[6] == 'Adm-clerical':
										return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '<=50K'
									elif obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Transport-moving':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Tech-support':
										return '<=50K'
									else: return '<=50K'
								else: return '<=50K'
							elif float(obj[0])>47.958340765792954:
								return '>50K'
							else: return '>50K'
						elif obj[7] == 'Other-relative':
							# {"feature": "workclass", "instances": 55, "metric_value": 0.1311, "depth": 7}
							if obj[1] == 'Private':
								return '<=50K'
							elif obj[1] == 'Self-emp-not-inc':
								# {"feature": "age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if float(obj[0])>26:
									return '<=50K'
								elif float(obj[0])<=26:
									return '>50K'
								else: return '>50K'
							elif obj[1] == 'Local-gov':
								return '<=50K'
							elif obj[1] == 'Self-emp-inc':
								return '<=50K'
							else: return '<=50K'
						else: return '<=50K'
					elif float(obj[11])>2339:
						return '>50K'
					else: return '>50K'
				else: return '<=50K'
			elif obj[5] == 'Divorced':
				# {"feature": "hours-per-week", "instances": 4268, "metric_value": 0.391, "depth": 4}
				if float(obj[12])<=41.03116213683224:
					# {"feature": "capital-loss", "instances": 3106, "metric_value": 0.2608, "depth": 5}
					if float(obj[11])<=986.4385866085296:
						# {"feature": "native-country", "instances": 3022, "metric_value": 0.25, "depth": 6}
						if obj[13] == 'United-States':
							# {"feature": "education", "instances": 2853, "metric_value": 0.2469, "depth": 7}
							if obj[3] == 'HS-grad':
								# {"feature": "age", "instances": 1130, "metric_value": 0.1628, "depth": 8}
								if float(obj[0])>31.81404259519988:
									# {"feature": "race", "instances": 959, "metric_value": 0.185, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "workclass", "instances": 809, "metric_value": 0.1989, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 661, "metric_value": 0.1881, "depth": 11}
											if obj[6] == 'Adm-clerical':
												# {"feature": "fnlwgt", "instances": 143, "metric_value": 0.1469, "depth": 12}
												if float(obj[2])>76686.27738568878:
													# {"feature": "relationship", "instances": 131, "metric_value": 0.114, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "sex", "instances": 59, "metric_value": 0.2136, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Not-in-family':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif float(obj[2])<=76686.27738568878:
													# {"feature": "relationship", "instances": 12, "metric_value": 0.4138, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "fnlwgt", "instances": 100, "metric_value": 0.2423, "depth": 12}
												if float(obj[2])>95226.07848514458:
													# {"feature": "relationship", "instances": 82, "metric_value": 0.1654, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 43, "metric_value": 0.2714, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif float(obj[2])<=95226.07848514458:
													# {"feature": "relationship", "instances": 18, "metric_value": 0.5033, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 12, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "fnlwgt", "instances": 71, "metric_value": 0.1851, "depth": 12}
												if float(obj[2])<=291723.7247913869:
													# {"feature": "relationship", "instances": 60, "metric_value": 0.1223, "depth": 13}
													if obj[7] == 'Not-in-family':
														return '<=50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "sex", "instances": 17, "metric_value": 0.3228, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif float(obj[2])>291723.7247913869:
													# {"feature": "sex", "instances": 11, "metric_value": 0.4395, "depth": 13}
													if obj[9] == 'Male':
														return '<=50K'
													elif obj[9] == 'Female':
														# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "fnlwgt", "instances": 54, "metric_value": 0.133, "depth": 12}
												if float(obj[2])<=304100.74614586926:
													return '<=50K'
												elif float(obj[2])>304100.74614586926:
													# {"feature": "relationship", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Not-in-family':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "sex", "instances": 50, "metric_value": 0.4022, "depth": 12}
												if obj[9] == 'Female':
													# {"feature": "fnlwgt", "instances": 41, "metric_value": 0.4612, "depth": 13}
													if float(obj[2])>23789:
														# {"feature": "relationship", "instances": 40, "metric_value": 0.469, "depth": 14}
														if obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Other-relative':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														else: return '<=50K'
													elif float(obj[2])<=23789:
														return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Male':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "sex", "instances": 47, "metric_value": 0.3425, "depth": 12}
												if obj[9] == 'Female':
													# {"feature": "relationship", "instances": 34, "metric_value": 0.4306, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "fnlwgt", "instances": 18, "metric_value": 0.3095, "depth": 14}
														if float(obj[2])<=162882:
															return '<=50K'
														elif float(obj[2])>162882:
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "fnlwgt", "instances": 14, "metric_value": 0.3712, "depth": 14}
														if float(obj[2])>137253:
															return '<=50K'
														elif float(obj[2])<=137253:
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 14}
														if float(obj[2])>114288:
															return '>50K'
														elif float(obj[2])<=114288:
															return '<=50K'
														else: return '<=50K'
													else: return '>50K'
												elif obj[9] == 'Male':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "fnlwgt", "instances": 31, "metric_value": 0.2056, "depth": 12}
												if float(obj[2])<=160361.70967741936:
													# {"feature": "relationship", "instances": 16, "metric_value": 0.3373, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 13, "metric_value": 0.3912, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													else: return '<=50K'
												elif float(obj[2])>160361.70967741936:
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											elif obj[6] == 'Tech-support':
												# {"feature": "sex", "instances": 12, "metric_value": 0.4138, "depth": 12}
												if obj[9] == 'Female':
													return '<=50K'
												elif obj[9] == 'Male':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Priv-house-serv':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Local-gov':
											# {"feature": "fnlwgt", "instances": 48, "metric_value": 0.4138, "depth": 11}
											if float(obj[2])>28151:
												# {"feature": "sex", "instances": 47, "metric_value": 0.3425, "depth": 12}
												if obj[9] == 'Female':
													return '<=50K'
												elif obj[9] == 'Male':
													# {"feature": "occupation", "instances": 13, "metric_value": 0.7793, "depth": 13}
													if obj[6] == 'Transport-moving':
														return '<=50K'
													elif obj[6] == 'Protective-serv':
														return '<=50K'
													elif obj[6] == 'Craft-repair':
														# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '>50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Farming-fishing':
														return '<=50K'
													elif obj[6] == 'Adm-clerical':
														return '<=50K'
													elif obj[6] == 'Tech-support':
														return '>50K'
													elif obj[6] == 'Handlers-cleaners':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif float(obj[2])<=28151:
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'State-gov':
											# {"feature": "occupation", "instances": 32, "metric_value": 0.3373, "depth": 11}
											if obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "fnlwgt", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if float(obj[2])>154117:
													return '<=50K'
												elif float(obj[2])<=154117:
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Protective-serv':
												# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 12}
												if float(obj[2])>94529:
													return '>50K'
												elif float(obj[2])<=94529:
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Federal-gov':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										else: return '<=50K'
									elif obj[8] == 'Black':
										# {"feature": "occupation", "instances": 131, "metric_value": 0.0647, "depth": 10}
										if obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[7] == 'Not-in-family':
												return '<=50K'
											elif obj[7] == 'Unmarried':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Priv-house-serv':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										else: return '<=50K'
									elif obj[8] == 'Amer-Indian-Eskimo':
										return '<=50K'
									elif obj[8] == 'Asian-Pac-Islander':
										return '<=50K'
									elif obj[8] == 'Other':
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Local-gov':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif float(obj[0])<=31.81404259519988:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Some-college':
								# {"feature": "sex", "instances": 720, "metric_value": 0.2108, "depth": 8}
								if obj[9] == 'Female':
									# {"feature": "fnlwgt", "instances": 539, "metric_value": 0.1437, "depth": 9}
									if float(obj[2])>63232.56696125193:
										# {"feature": "relationship", "instances": 478, "metric_value": 0.1102, "depth": 10}
										if obj[7] == 'Unmarried':
											# {"feature": "workclass", "instances": 243, "metric_value": 0.0385, "depth": 11}
											if obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "occupation", "instances": 16, "metric_value": 0.3373, "depth": 12}
												if obj[6] == 'Adm-clerical':
													return '<=50K'
												elif obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '>50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Not-in-family':
											# {"feature": "occupation", "instances": 190, "metric_value": 0.1473, "depth": 11}
											if obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "age", "instances": 35, "metric_value": 0.1872, "depth": 12}
												if float(obj[0])>44.57142857142857:
													return '<=50K'
												elif float(obj[0])<=44.57142857142857:
													# {"feature": "race", "instances": 16, "metric_value": 0.3373, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "workclass", "instances": 12, "metric_value": 0.4138, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														elif obj[1] == 'Self-emp-not-inc':
															return '<=50K'
														elif obj[1] == 'State-gov':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "age", "instances": 28, "metric_value": 0.2223, "depth": 12}
												if float(obj[0])<=55.94105378207861:
													return '<=50K'
												elif float(obj[0])>55.94105378207861:
													# {"feature": "workclass", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Other-service':
												# {"feature": "age", "instances": 14, "metric_value": 0.3712, "depth": 12}
												if float(obj[0])>41:
													return '<=50K'
												elif float(obj[0])<=41:
													# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Tech-support':
												# {"feature": "workclass", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Own-child':
											return '<=50K'
										elif obj[7] == 'Other-relative':
											# {"feature": "workclass", "instances": 12, "metric_value": 0.65, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "age", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if float(obj[0])<=47:
													return '<=50K'
												elif float(obj[0])>47:
													# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Priv-house-serv':
														return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Sales':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '>50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif float(obj[2])<=63232.56696125193:
										# {"feature": "race", "instances": 61, "metric_value": 0.3492, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "relationship", "instances": 54, "metric_value": 0.2285, "depth": 11}
											if obj[7] == 'Unmarried':
												return '<=50K'
											elif obj[7] == 'Not-in-family':
												# {"feature": "age", "instances": 26, "metric_value": 0.3912, "depth": 12}
												if float(obj[0])>37:
													return '<=50K'
												elif float(obj[0])<=37:
													# {"feature": "occupation", "instances": 10, "metric_value": 0.7219, "depth": 13}
													if obj[6] == 'Adm-clerical':
														# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '>50K'
													elif obj[6] == 'Sales':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'Amer-Indian-Eskimo':
											# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[1] == 'Federal-gov':
												return '<=50K'
											elif obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Black':
											# {"feature": "age", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if float(obj[0])>36:
												return '<=50K'
											elif float(obj[0])<=36:
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									else: return '<=50K'
								elif obj[9] == 'Male':
									# {"feature": "race", "instances": 181, "metric_value": 0.3727, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "occupation", "instances": 162, "metric_value": 0.403, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "fnlwgt", "instances": 45, "metric_value": 0.5665, "depth": 11}
											if float(obj[2])>40151:
												# {"feature": "workclass", "instances": 44, "metric_value": 0.5108, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "age", "instances": 34, "metric_value": 0.6024, "depth": 13}
													if float(obj[0])>21:
														# {"feature": "relationship", "instances": 33, "metric_value": 0.6136, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														else: return '<=50K'
													elif float(obj[0])<=21:
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])<=40151:
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "age", "instances": 17, "metric_value": 0.5226, "depth": 11}
											if float(obj[0])>39:
												return '<=50K'
											elif float(obj[0])<=39:
												# {"feature": "relationship", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Own-child':
													return '<=50K'
												elif obj[7] == 'Not-in-family':
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'Private':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											# {"feature": "fnlwgt", "instances": 14, "metric_value": 0.3712, "depth": 11}
											if float(obj[2])<=227160:
												return '<=50K'
											elif float(obj[2])>227160:
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "age", "instances": 10, "metric_value": 0.7219, "depth": 11}
											if float(obj[0])<=47:
												# {"feature": "fnlwgt", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if float(obj[2])<=294919:
													return '<=50K'
												elif float(obj[2])>294919:
													return '>50K'
												else: return '>50K'
											elif float(obj[0])>47:
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											# {"feature": "age", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if float(obj[0])>43:
												return '<=50K'
											elif float(obj[0])<=43:
												# {"feature": "fnlwgt", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if float(obj[2])>183765:
													return '<=50K'
												elif float(obj[2])<=183765:
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "age", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if float(obj[0])>31:
												return '<=50K'
											elif float(obj[0])<=31:
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[8] == 'Black':
										return '<=50K'
									elif obj[8] == 'Amer-Indian-Eskimo':
										return '<=50K'
									elif obj[8] == 'Asian-Pac-Islander':
										return '<=50K'
									else: return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Bachelors':
								# {"feature": "fnlwgt", "instances": 271, "metric_value": 0.4678, "depth": 8}
								if float(obj[2])>88653.44999138112:
									# {"feature": "age", "instances": 236, "metric_value": 0.5131, "depth": 9}
									if float(obj[0])<=64.11431149021615:
										# {"feature": "occupation", "instances": 228, "metric_value": 0.5248, "depth": 10}
										if obj[6] == 'Prof-specialty':
											# {"feature": "workclass", "instances": 78, "metric_value": 0.4771, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "sex", "instances": 33, "metric_value": 0.4395, "depth": 12}
												if obj[9] == 'Female':
													# {"feature": "race", "instances": 25, "metric_value": 0.5294, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "relationship", "instances": 20, "metric_value": 0.6098, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													elif obj[8] == 'Other':
														return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Male':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "race", "instances": 27, "metric_value": 0.3809, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 21, "metric_value": 0.4537, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "relationship", "instances": 17, "metric_value": 0.5226, "depth": 14}
														if obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														elif obj[7] == 'Other-relative':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Other-relative':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "workclass", "instances": 53, "metric_value": 0.6573, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 34, "metric_value": 0.6723, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 31, "metric_value": 0.6374, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "relationship", "instances": 19, "metric_value": 0.4855, "depth": 14}
														if obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														# {"feature": "relationship", "instances": 12, "metric_value": 0.8113, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '>50K'
														elif obj[7] == 'Other-relative':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Not-in-family':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'State-gov':
												# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[9] == 'Female':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Male':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Unmarried':
													return '<=50K'
												elif obj[7] == 'Not-in-family':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Female':
														return '>50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "relationship", "instances": 32, "metric_value": 0.4489, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "sex", "instances": 19, "metric_value": 0.2975, "depth": 12}
												if obj[9] == 'Female':
													return '<=50K'
												elif obj[9] == 'Male':
													# {"feature": "workclass", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Unmarried':
												# {"feature": "workclass", "instances": 11, "metric_value": 0.4395, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "sex", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "race", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Own-child':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Federal-gov':
													return '<=50K'
												elif obj[1] == 'Private':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											# {"feature": "sex", "instances": 20, "metric_value": 0.8113, "depth": 11}
											if obj[9] == 'Female':
												# {"feature": "race", "instances": 12, "metric_value": 0.4138, "depth": 12}
												if obj[8] == 'White':
													return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[9] == 'Male':
												# {"feature": "workclass", "instances": 8, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											else: return '>50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "workclass", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[1] == 'Local-gov':
												# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Private':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Priv-house-serv':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[0])>64.11431149021615:
										return '<=50K'
									else: return '<=50K'
								elif float(obj[2])<=88653.44999138112:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Assoc-voc':
								# {"feature": "workclass", "instances": 168, "metric_value": 0.3256, "depth": 8}
								if obj[1] == 'Private':
									# {"feature": "occupation", "instances": 131, "metric_value": 0.2683, "depth": 9}
									if obj[6] == 'Prof-specialty':
										# {"feature": "age", "instances": 29, "metric_value": 0.5788, "depth": 10}
										if float(obj[0])<=54.62505926147348:
											# {"feature": "fnlwgt", "instances": 25, "metric_value": 0.6343, "depth": 11}
											if float(obj[2])>46155:
												# {"feature": "race", "instances": 24, "metric_value": 0.5436, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 23, "metric_value": 0.5586, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "relationship", "instances": 18, "metric_value": 0.5033, "depth": 14}
														if obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Not-in-family':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])<=46155:
												return '>50K'
											else: return '>50K'
										elif float(obj[0])>54.62505926147348:
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Adm-clerical':
										return '<=50K'
									elif obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Tech-support':
										return '<=50K'
									elif obj[6] == 'Sales':
										# {"feature": "fnlwgt", "instances": 14, "metric_value": 0.3712, "depth": 10}
										if float(obj[2])<=199448:
											return '<=50K'
										elif float(obj[2])>199448:
											# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if float(obj[0])>30:
												return '<=50K'
											elif float(obj[0])<=30:
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[6] == 'Craft-repair':
										return '<=50K'
									elif obj[6] == 'Exec-managerial':
										# {"feature": "age", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if float(obj[0])<=42:
											return '<=50K'
										elif float(obj[0])>42:
											# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 11}
											if float(obj[2])<=102147:
												return '>50K'
											elif float(obj[2])>102147:
												return '<=50K'
											else: return '<=50K'
										else: return '>50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Transport-moving':
										return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Protective-serv':
										return '<=50K'
									else: return '<=50K'
								elif obj[1] == 'Local-gov':
									# {"feature": "age", "instances": 13, "metric_value": 0.3912, "depth": 9}
									if float(obj[0])<=59:
										return '<=50K'
									elif float(obj[0])>59:
										# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 10}
										if float(obj[2])>101110:
											return '<=50K'
										elif float(obj[2])<=101110:
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif obj[1] == 'Federal-gov':
									# {"feature": "fnlwgt", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if float(obj[2])>206553:
										# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[7] == 'Unmarried':
											return '>50K'
										elif obj[7] == 'Not-in-family':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[2])<=206553:
										return '<=50K'
									else: return '<=50K'
								elif obj[1] == 'Self-emp-not-inc':
									return '<=50K'
								elif obj[1] == 'State-gov':
									return '<=50K'
								elif obj[1] == 'Self-emp-inc':
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Assoc-acdm':
								# {"feature": "age", "instances": 129, "metric_value": 0.1994, "depth": 8}
								if float(obj[0])<=59.45336467053074:
									# {"feature": "fnlwgt", "instances": 125, "metric_value": 0.1633, "depth": 9}
									if float(obj[2])>181391.64:
										# {"feature": "occupation", "instances": 63, "metric_value": 0.2762, "depth": 10}
										if obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											# {"feature": "relationship", "instances": 11, "metric_value": 0.4395, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "workclass", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Unmarried':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "relationship", "instances": 10, "metric_value": 0.7219, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "workclass", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Unmarried':
												return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Sales':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[2])<=181391.64:
										return '<=50K'
									else: return '<=50K'
								elif float(obj[0])>59.45336467053074:
									# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[9] == 'Female':
										return '<=50K'
									elif obj[9] == 'Male':
										return '>50K'
									else: return '>50K'
								else: return '<=50K'
							elif obj[3] == 'Masters':
								# {"feature": "age", "instances": 115, "metric_value": 0.6858, "depth": 8}
								if float(obj[0])>39.4494220010878:
									# {"feature": "fnlwgt", "instances": 101, "metric_value": 0.7375, "depth": 9}
									if float(obj[2])<=368382.1598696073:
										# {"feature": "occupation", "instances": 97, "metric_value": 0.7136, "depth": 10}
										if obj[6] == 'Prof-specialty':
											# {"feature": "race", "instances": 65, "metric_value": 0.6559, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "relationship", "instances": 57, "metric_value": 0.6292, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "workclass", "instances": 37, "metric_value": 0.7532, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 12, "metric_value": 0.65, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 12, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '>50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													# {"feature": "workclass", "instances": 19, "metric_value": 0.2975, "depth": 13}
													if obj[1] == 'Local-gov':
														# {"feature": "sex", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Private':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												# {"feature": "workclass", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'State-gov':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "workclass", "instances": 15, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "sex", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[9] == 'Female':
													# {"feature": "relationship", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[9] == 'Male':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Sales':
											# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[9] == 'Female':
												# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Male':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '>50K'
										elif obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[2])>368382.1598696073:
										# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[7] == 'Unmarried':
											return '>50K'
										elif obj[7] == 'Not-in-family':
											return '<=50K'
										else: return '<=50K'
									else: return '>50K'
								elif float(obj[0])<=39.4494220010878:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == '11th':
								# {"feature": "race", "instances": 92, "metric_value": 0.2073, "depth": 8}
								if obj[8] == 'White':
									# {"feature": "occupation", "instances": 73, "metric_value": 0.1812, "depth": 9}
									if obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Sales':
										return '<=50K'
									elif obj[6] == 'Craft-repair':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Adm-clerical':
										# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[9] == 'Female':
											return '<=50K'
										elif obj[9] == 'Male':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Exec-managerial':
										# {"feature": "fnlwgt", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if float(obj[2])>83446:
											return '<=50K'
										elif float(obj[2])<=83446:
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Transport-moving':
										return '<=50K'
									elif obj[6] == 'Farming-fishing':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '<=50K'
									elif obj[6] == 'Protective-serv':
										return '<=50K'
									else: return '<=50K'
								elif obj[8] == 'Black':
									return '<=50K'
								elif obj[8] == 'Other':
									return '<=50K'
								elif obj[8] == 'Asian-Pac-Islander':
									return '<=50K'
								elif obj[8] == 'Amer-Indian-Eskimo':
									return '>50K'
								else: return '>50K'
							elif obj[3] == '10th':
								return '<=50K'
							elif obj[3] == '7th-8th':
								return '<=50K'
							elif obj[3] == '9th':
								# {"feature": "age", "instances": 49, "metric_value": 0.1437, "depth": 8}
								if float(obj[0])<=46.48979591836735:
									return '<=50K'
								elif float(obj[0])>46.48979591836735:
									# {"feature": "fnlwgt", "instances": 24, "metric_value": 0.2499, "depth": 9}
									if float(obj[2])>101471.70882830949:
										return '<=50K'
									elif float(obj[2])<=101471.70882830949:
										# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Craft-repair':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								else: return '<=50K'
							elif obj[3] == '12th':
								return '<=50K'
							elif obj[3] == '5th-6th':
								return '<=50K'
							elif obj[3] == '1st-4th':
								return '<=50K'
							else: return '<=50K'
						elif obj[13] == 'Mexico':
							# {"feature": "workclass", "instances": 17, "metric_value": 0.3228, "depth": 7}
							if obj[1] == 'Private':
								return '<=50K'
							elif obj[1] == 'Local-gov':
								return '<=50K'
							elif obj[1] == 'State-gov':
								return '>50K'
							elif obj[1] == 'Self-emp-not-inc':
								return '<=50K'
							else: return '<=50K'
						elif obj[13] == 'Germany':
							# {"feature": "sex", "instances": 16, "metric_value": 0.5436, "depth": 7}
							if obj[9] == 'Female':
								return '<=50K'
							elif obj[9] == 'Male':
								return '>50K'
							else: return '>50K'
						elif obj[13] == 'Canada':
							return '<=50K'
						elif obj[13] == 'Puerto-Rico':
							# {"feature": "age", "instances": 12, "metric_value": 0.65, "depth": 7}
							if float(obj[0])<=60:
								# {"feature": "fnlwgt", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if float(obj[2])<=270278:
									return '<=50K'
								elif float(obj[2])>270278:
									return '>50K'
								else: return '>50K'
							elif float(obj[0])>60:
								return '>50K'
							else: return '>50K'
						elif obj[13] == 'Cuba':
							return '<=50K'
						elif obj[13] == 'England':
							return '<=50K'
						elif obj[13] == 'Philippines':
							# {"feature": "workclass", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[1] == 'Private':
								return '<=50K'
							elif obj[1] == 'Federal-gov':
								# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if float(obj[0])>35:
									return '>50K'
								elif float(obj[0])<=35:
									return '<=50K'
								else: return '<=50K'
							else: return '>50K'
						elif obj[13] == 'Dominican-Republic':
							return '<=50K'
						elif obj[13] == 'Japan':
							# {"feature": "fnlwgt", "instances": 6, "metric_value": 0.65, "depth": 7}
							if float(obj[2])>60722:
								return '<=50K'
							elif float(obj[2])<=60722:
								return '>50K'
							else: return '>50K'
						elif obj[13] == 'Columbia':
							return '<=50K'
						elif obj[13] == 'China':
							return '<=50K'
						elif obj[13] == 'Jamaica':
							return '<=50K'
						elif obj[13] == 'South':
							return '<=50K'
						elif obj[13] == 'Guatemala':
							# {"feature": "age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if float(obj[0])>40:
								return '<=50K'
							elif float(obj[0])<=40:
								return '>50K'
							else: return '>50K'
						elif obj[13] == 'Portugal':
							return '<=50K'
						elif obj[13] == 'Italy':
							return '<=50K'
						elif obj[13] == 'Honduras':
							return '<=50K'
						elif obj[13] == 'Poland':
							return '<=50K'
						elif obj[13] == 'El-Salvador':
							return '<=50K'
						elif obj[13] == 'Iran':
							return '<=50K'
						elif obj[13] == 'Haiti':
							return '<=50K'
						elif obj[13] == 'Vietnam':
							return '<=50K'
						elif obj[13] == 'Ecuador':
							return '<=50K'
						elif obj[13] == 'Trinadad&Tobago':
							return '<=50K'
						elif obj[13] == 'Outlying-US(Guam-USVI-etc)':
							return '<=50K'
						elif obj[13] == 'Peru':
							return '<=50K'
						elif obj[13] == 'France':
							return '<=50K'
						elif obj[13] == 'Nicaragua':
							return '<=50K'
						elif obj[13] == 'Ireland':
							return '<=50K'
						elif obj[13] == 'Hungary':
							return '>50K'
						elif obj[13] == 'Scotland':
							return '<=50K'
						elif obj[13] == 'Yugoslavia':
							return '<=50K'
						elif obj[13] == 'Taiwan':
							return '<=50K'
						else: return '<=50K'
					elif float(obj[11])>986.4385866085296:
						# {"feature": "age", "instances": 84, "metric_value": 0.56, "depth": 6}
						if float(obj[0])<=54.67314267484194:
							# {"feature": "education", "instances": 71, "metric_value": 0.622, "depth": 7}
							if obj[3] == 'HS-grad':
								# {"feature": "sex", "instances": 26, "metric_value": 0.2352, "depth": 8}
								if obj[9] == 'Male':
									return '<=50K'
								elif obj[9] == 'Female':
									# {"feature": "fnlwgt", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if float(obj[2])>175070:
										return '<=50K'
									elif float(obj[2])<=175070:
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Exec-managerial':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										else: return '<=50K'
									else: return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Bachelors':
								# {"feature": "fnlwgt", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if float(obj[2])>29591:
									# {"feature": "relationship", "instances": 13, "metric_value": 0.7793, "depth": 9}
									if obj[7] == 'Not-in-family':
										# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 10}
										if obj[9] == 'Male':
											# {"feature": "workclass", "instances": 9, "metric_value": 0.7642, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[6] == 'Sales':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[9] == 'Female':
											return '<=50K'
										else: return '<=50K'
									elif obj[7] == 'Own-child':
										return '<=50K'
									elif obj[7] == 'Unmarried':
										return '>50K'
									else: return '>50K'
								elif float(obj[2])<=29591:
									return '>50K'
								else: return '>50K'
							elif obj[3] == 'Some-college':
								# {"feature": "relationship", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[7] == 'Not-in-family':
									return '<=50K'
								elif obj[7] == 'Own-child':
									return '<=50K'
								elif obj[7] == 'Unmarried':
									# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'Private':
										return '>50K'
									elif obj[1] == 'State-gov':
										return '<=50K'
									else: return '<=50K'
								else: return '>50K'
							elif obj[3] == 'Masters':
								# {"feature": "fnlwgt", "instances": 6, "metric_value": 1.0, "depth": 8}
								if float(obj[2])>44121:
									# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[6] == 'Prof-specialty':
										# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7] == 'Unmarried':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Not-in-family':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Exec-managerial':
										return '>50K'
									else: return '>50K'
								elif float(obj[2])<=44121:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Assoc-acdm':
								# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[1] == 'Private':
									return '<=50K'
								elif obj[1] == 'Federal-gov':
									return '<=50K'
								elif obj[1] == 'State-gov':
									return '>50K'
								else: return '>50K'
							elif obj[3] == '7th-8th':
								return '<=50K'
							elif obj[3] == 'Assoc-voc':
								# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1] == 'State-gov':
									return '>50K'
								elif obj[1] == 'Private':
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == '11th':
								return '<=50K'
							elif obj[3] == '10th':
								return '<=50K'
							elif obj[3] == '9th':
								return '<=50K'
							else: return '<=50K'
						elif float(obj[0])>54.67314267484194:
							return '<=50K'
						else: return '<=50K'
					else: return '<=50K'
				elif float(obj[12])>41.03116213683224:
					# {"feature": "native-country", "instances": 1162, "metric_value": 0.6447, "depth": 5}
					if obj[13] == 'United-States':
						# {"feature": "age", "instances": 1107, "metric_value": 0.6426, "depth": 6}
						if float(obj[0])>23.65729472963945:
							# {"feature": "fnlwgt", "instances": 1097, "metric_value": 0.6461, "depth": 7}
							if float(obj[2])>19410:
								# {"feature": "education", "instances": 1096, "metric_value": 0.6465, "depth": 8}
								if obj[3] == 'HS-grad':
									# {"feature": "capital-loss", "instances": 353, "metric_value": 0.4291, "depth": 9}
									if float(obj[11])<=1980:
										# {"feature": "occupation", "instances": 350, "metric_value": 0.422, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "race", "instances": 65, "metric_value": 0.4929, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "relationship", "instances": 59, "metric_value": 0.4187, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "workclass", "instances": 38, "metric_value": 0.4855, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 28, "metric_value": 0.2223, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												elif obj[7] == 'Other-relative':
													return '>50K'
												else: return '>50K'
											elif obj[8] == 'Black':
												# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Private':
														return '>50K'
													else: return '>50K'
												elif obj[9] == 'Female':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Amer-Indian-Eskimo':
												# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											# {"feature": "relationship", "instances": 53, "metric_value": 0.4508, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "race", "instances": 32, "metric_value": 0.6253, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "workclass", "instances": 28, "metric_value": 0.6769, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "sex", "instances": 20, "metric_value": 0.6098, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												elif obj[8] == 'Black':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Unmarried':
												return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											# {"feature": "sex", "instances": 49, "metric_value": 0.4079, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "relationship", "instances": 47, "metric_value": 0.3425, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "workclass", "instances": 39, "metric_value": 0.2918, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 33, "metric_value": 0.3298, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Unmarried':
													return '<=50K'
												elif obj[7] == 'Not-in-family':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif obj[6] == 'Sales':
											# {"feature": "workclass", "instances": 47, "metric_value": 0.4889, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 32, "metric_value": 0.3373, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 25, "metric_value": 0.4022, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 24, "metric_value": 0.4138, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "relationship", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[9] == 'Male':
													return '<=50K'
												elif obj[9] == 'Female':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														elif obj[8] == 'Asian-Pac-Islander':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Not-in-family':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "workclass", "instances": 45, "metric_value": 0.1537, "depth": 11}
											if obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'State-gov':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Unmarried':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Other-service':
											# {"feature": "relationship", "instances": 18, "metric_value": 0.3095, "depth": 11}
											if obj[7] == 'Not-in-family':
												return '<=50K'
											elif obj[7] == 'Unmarried':
												# {"feature": "workclass", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "relationship", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "workclass", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Tech-support':
											# {"feature": "sex", "instances": 10, "metric_value": 0.971, "depth": 11}
											if obj[9] == 'Female':
												# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Male':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Not-in-family':
													return '>50K'
												elif obj[7] == 'Unmarried':
													return '>50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											else: return '>50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											# {"feature": "workclass", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[1] == 'Local-gov':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Priv-house-serv':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[11])>1980:
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif obj[3] == 'Some-college':
									# {"feature": "capital-loss", "instances": 273, "metric_value": 0.5525, "depth": 9}
									if float(obj[11])<=0:
										# {"feature": "sex", "instances": 263, "metric_value": 0.5658, "depth": 10}
										if obj[9] == 'Male':
											# {"feature": "occupation", "instances": 140, "metric_value": 0.6769, "depth": 11}
											if obj[6] == 'Craft-repair':
												# {"feature": "relationship", "instances": 27, "metric_value": 0.6052, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "workclass", "instances": 21, "metric_value": 0.5917, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 17, "metric_value": 0.6723, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												elif obj[7] == 'Own-child':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "workclass", "instances": 26, "metric_value": 0.8905, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 15, "metric_value": 0.5665, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Sales':
												# {"feature": "workclass", "instances": 18, "metric_value": 0.7642, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 14, "metric_value": 0.5917, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Own-child':
														return '>50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Machine-op-inspct':
												# {"feature": "relationship", "instances": 13, "metric_value": 0.3912, "depth": 12}
												if obj[7] == 'Not-in-family':
													return '<=50K'
												elif obj[7] == 'Unmarried':
													# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "workclass", "instances": 12, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 10, "metric_value": 0.469, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Local-gov':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Other-service':
												# {"feature": "race", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[8] == 'White':
													return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "race", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if obj[8] == 'White':
													return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "workclass", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Handlers-cleaners':
												# {"feature": "workclass", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											else: return '<=50K'
										elif obj[9] == 'Female':
											# {"feature": "workclass", "instances": 123, "metric_value": 0.4067, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 97, "metric_value": 0.4787, "depth": 12}
												if obj[6] == 'Adm-clerical':
													# {"feature": "race", "instances": 35, "metric_value": 0.316, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "relationship", "instances": 33, "metric_value": 0.1959, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '>50K'
														else: return '>50K'
													elif obj[8] == 'Asian-Pac-Islander':
														return '<=50K'
													elif obj[8] == 'Black':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Exec-managerial':
													# {"feature": "relationship", "instances": 20, "metric_value": 0.6098, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Other-relative':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Sales':
													# {"feature": "relationship", "instances": 19, "metric_value": 0.6292, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 10, "metric_value": 0.7219, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Other-service':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Handlers-cleaners':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												elif obj[6] == 'Machine-op-inspct':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												return '<=50K'
											elif obj[1] == 'Local-gov':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif float(obj[11])>0:
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == 'Bachelors':
									# {"feature": "capital-loss", "instances": 194, "metric_value": 0.9148, "depth": 9}
									if float(obj[11])<=1980:
										# {"feature": "workclass", "instances": 192, "metric_value": 0.9075, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 122, "metric_value": 0.9617, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "race", "instances": 45, "metric_value": 0.9996, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "relationship", "instances": 40, "metric_value": 0.9982, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 29, "metric_value": 0.9923, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "sex", "instances": 9, "metric_value": 0.9911, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Own-child':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '>50K'
												elif obj[8] == 'Black':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Unmarried':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Not-in-family':
														return '>50K'
													else: return '>50K'
												elif obj[8] == 'Amer-Indian-Eskimo':
													return '<=50K'
												elif obj[8] == 'Asian-Pac-Islander':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												# {"feature": "sex", "instances": 28, "metric_value": 0.8113, "depth": 12}
												if obj[9] == 'Female':
													# {"feature": "relationship", "instances": 18, "metric_value": 0.65, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 12, "metric_value": 0.65, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														return '<=50K'
													else: return '<=50K'
												elif obj[9] == 'Male':
													# {"feature": "relationship", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "sex", "instances": 28, "metric_value": 0.9403, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "race", "instances": 19, "metric_value": 0.998, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "relationship", "instances": 17, "metric_value": 0.9774, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														elif obj[7] == 'Unmarried':
															return '<=50K'
														elif obj[7] == 'Own-child':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Amer-Indian-Eskimo':
														return '>50K'
													elif obj[8] == 'Black':
														return '>50K'
													else: return '>50K'
												elif obj[9] == 'Female':
													# {"feature": "relationship", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "sex", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[9] == 'Female':
													return '<=50K'
												elif obj[9] == 'Male':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Black':
														return '<=50K'
													elif obj[8] == 'White':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Female':
														return '<=50K'
													elif obj[9] == 'Male':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Unmarried':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Protective-serv':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													return '<=50K'
												elif obj[8] == 'Black':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Handlers-cleaners':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Transport-moving':
												return '<=50K'
											elif obj[6] == 'Tech-support':
												return '>50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Local-gov':
											# {"feature": "occupation", "instances": 23, "metric_value": 0.4262, "depth": 11}
											if obj[6] == 'Prof-specialty':
												# {"feature": "relationship", "instances": 20, "metric_value": 0.2864, "depth": 12}
												if obj[7] == 'Unmarried':
													# {"feature": "sex", "instances": 12, "metric_value": 0.4138, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "race", "instances": 10, "metric_value": 0.469, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Not-in-family':
													return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '>50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Exec-managerial':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "sex", "instances": 20, "metric_value": 0.7219, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "occupation", "instances": 16, "metric_value": 0.8113, "depth": 12}
												if obj[6] == 'Exec-managerial':
													# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[7] == 'Not-in-family':
														return '<=50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Sales':
													# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Transport-moving':
													return '<=50K'
												elif obj[6] == 'Other-service':
													return '>50K'
												else: return '>50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											# {"feature": "sex", "instances": 15, "metric_value": 0.7219, "depth": 11}
											if obj[9] == 'Male':
												# {"feature": "occupation", "instances": 11, "metric_value": 0.8454, "depth": 12}
												if obj[6] == 'Exec-managerial':
													# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '>50K'
													else: return '>50K'
												elif obj[6] == 'Sales':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												elif obj[6] == 'Farming-fishing':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Female':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Federal-gov':
											# {"feature": "relationship", "instances": 9, "metric_value": 0.9183, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[6] == 'Exec-managerial':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[6] == 'Protective-serv':
													return '>50K'
												elif obj[6] == 'Prof-specialty':
													return '>50K'
												else: return '>50K'
											elif obj[7] == 'Unmarried':
												# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[6] == 'Exec-managerial':
													return '>50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'State-gov':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[11])>1980:
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Masters':
									# {"feature": "capital-loss", "instances": 84, "metric_value": 0.9403, "depth": 9}
									if float(obj[11])<=2339:
										# {"feature": "race", "instances": 83, "metric_value": 0.9335, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "occupation", "instances": 79, "metric_value": 0.914, "depth": 11}
											if obj[6] == 'Prof-specialty':
												# {"feature": "workclass", "instances": 38, "metric_value": 0.5618, "depth": 12}
												if obj[1] == 'Local-gov':
													return '<=50K'
												elif obj[1] == 'Private':
													# {"feature": "relationship", "instances": 14, "metric_value": 0.5917, "depth": 13}
													if obj[7] == 'Not-in-family':
														return '<=50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "sex", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Own-child':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "workclass", "instances": 29, "metric_value": 0.9784, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 19, "metric_value": 0.9819, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 11, "metric_value": 0.8454, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														elif obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Unmarried':
														# {"feature": "sex", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Local-gov':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														else: return '>50K'
													elif obj[7] == 'Unmarried':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														return '<=50K'
													elif obj[7] == 'Unmarried':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-not-inc':
													return '>50K'
												elif obj[1] == 'Self-emp-inc':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														return '>50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												else: return '>50K'
											elif obj[6] == 'Sales':
												# {"feature": "workclass", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Private':
													# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'Self-emp-inc':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Protective-serv':
												# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'State-gov':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											else: return '<=50K'
										elif obj[8] == 'Black':
											# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Local-gov':
												return '>50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											elif obj[1] == 'Private':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Amer-Indian-Eskimo':
											return '>50K'
										else: return '>50K'
									elif float(obj[11])>2339:
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Assoc-acdm':
									# {"feature": "capital-loss", "instances": 55, "metric_value": 0.5499, "depth": 9}
									if float(obj[11])<=880:
										# {"feature": "workclass", "instances": 54, "metric_value": 0.5033, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "sex", "instances": 40, "metric_value": 0.469, "depth": 11}
											if obj[9] == 'Female':
												# {"feature": "relationship", "instances": 25, "metric_value": 0.2423, "depth": 12}
												if obj[7] == 'Not-in-family':
													return '<=50K'
												elif obj[7] == 'Unmarried':
													# {"feature": "occupation", "instances": 10, "metric_value": 0.469, "depth": 13}
													if obj[6] == 'Exec-managerial':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Sales':
														return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Adm-clerical':
														return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Male':
												# {"feature": "relationship", "instances": 15, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "occupation", "instances": 13, "metric_value": 0.6194, "depth": 13}
													if obj[6] == 'Sales':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Craft-repair':
														# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Black':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Machine-op-inspct':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '>50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Local-gov':
											# {"feature": "occupation", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Protective-serv':
												# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == 'Male':
													return '<=50K'
												elif obj[9] == 'Female':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Federal-gov':
											return '>50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[11])>880:
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Assoc-voc':
									# {"feature": "race", "instances": 52, "metric_value": 0.6194, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "workclass", "instances": 46, "metric_value": 0.6666, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "occupation", "instances": 32, "metric_value": 0.6962, "depth": 11}
											if obj[6] == 'Exec-managerial':
												# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[9] == 'Female':
													return '<=50K'
												elif obj[9] == 'Male':
													# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "capital-loss", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if float(obj[11])<=0:
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'Not-in-family':
													return '<=50K'
												elif obj[7] == 'Unmarried':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "capital-loss", "instances": 2, "metric_value": 1.0, "depth": 14}
														if float(obj[11])<=0:
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Sales':
												# {"feature": "relationship", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "capital-loss", "instances": 4, "metric_value": 1.0, "depth": 14}
														if float(obj[11])<=0:
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[7] == 'Own-child':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											elif obj[6] == 'Craft-repair':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Own-child':
													return '<=50K'
												elif obj[7] == 'Unmarried':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Transport-moving':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "capital-loss", "instances": 2, "metric_value": 1.0, "depth": 14}
														if float(obj[11])<=0:
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[6] == 'Machine-op-inspct':
												return '<=50K'
											elif obj[6] == 'Handlers-cleaners':
												return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Local-gov':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == 'Exec-managerial':
												return '<=50K'
											elif obj[6] == 'Sales':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'State-gov':
											# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'Prof-specialty':
												return '>50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											else: return '<=50K'
										else: return '>50K'
									elif obj[8] == 'Black':
										return '<=50K'
									elif obj[8] == 'Amer-Indian-Eskimo':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == '11th':
									# {"feature": "capital-loss", "instances": 27, "metric_value": 0.5033, "depth": 9}
									if float(obj[11])<=1876:
										# {"feature": "occupation", "instances": 26, "metric_value": 0.3912, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "relationship", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[7] == 'Not-in-family':
												return '<=50K'
											elif obj[7] == 'Own-child':
												# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == 'Female':
													return '>50K'
												elif obj[9] == 'Male':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Unmarried':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Sales':
											# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Not-in-family':
												return '>50K'
											elif obj[7] == 'Unmarried':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[11])>1876:
										return '>50K'
									else: return '>50K'
								elif obj[3] == '10th':
									# {"feature": "relationship", "instances": 27, "metric_value": 0.2285, "depth": 9}
									if obj[7] == 'Not-in-family':
										return '<=50K'
									elif obj[7] == 'Unmarried':
										return '<=50K'
									elif obj[7] == 'Own-child':
										return '>50K'
									else: return '>50K'
								elif obj[3] == '7th-8th':
									return '<=50K'
								elif obj[3] == '9th':
									return '<=50K'
								elif obj[3] == '12th':
									# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "relationship", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[7] == 'Not-in-family':
											# {"feature": "capital-loss", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if float(obj[11])<=0:
												return '>50K'
											elif float(obj[11])>0:
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Unmarried':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == '5th-6th':
									return '<=50K'
								else: return '<=50K'
							elif float(obj[2])<=19410:
								return '<=50K'
							else: return '<=50K'
						elif float(obj[0])<=23.65729472963945:
							return '<=50K'
						else: return '<=50K'
					elif obj[13] == 'Germany':
						return '<=50K'
					elif obj[13] == 'England':
						# {"feature": "fnlwgt", "instances": 6, "metric_value": 1.0, "depth": 6}
						if float(obj[2])<=87205:
							return '<=50K'
						elif float(obj[2])>87205:
							return '>50K'
						else: return '>50K'
					elif obj[13] == 'Mexico':
						return '<=50K'
					elif obj[13] == 'Canada':
						return '<=50K'
					elif obj[13] == 'Iran':
						# {"feature": "fnlwgt", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if float(obj[2])<=190483:
							return '<=50K'
						elif float(obj[2])>190483:
							return '>50K'
						else: return '>50K'
					elif obj[13] == 'Japan':
						# {"feature": "fnlwgt", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if float(obj[2])>124685:
							return '<=50K'
						elif float(obj[2])<=124685:
							return '>50K'
						else: return '>50K'
					elif obj[13] == 'France':
						return '<=50K'
					elif obj[13] == 'Puerto-Rico':
						# {"feature": "fnlwgt", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if float(obj[2])<=109339:
							return '<=50K'
						elif float(obj[2])>109339:
							return '>50K'
						else: return '>50K'
					elif obj[13] == 'India':
						return '>50K'
					elif obj[13] == 'South':
						return '>50K'
					elif obj[13] == 'Cuba':
						return '<=50K'
					elif obj[13] == 'Columbia':
						return '<=50K'
					elif obj[13] == 'Outlying-US(Guam-USVI-etc)':
						return '<=50K'
					elif obj[13] == 'Ireland':
						return '<=50K'
					elif obj[13] == 'Vietnam':
						return '<=50K'
					elif obj[13] == 'Haiti':
						return '<=50K'
					elif obj[13] == 'Poland':
						return '<=50K'
					elif obj[13] == 'El-Salvador':
						return '<=50K'
					elif obj[13] == 'Thailand':
						return '<=50K'
					elif obj[13] == 'Dominican-Republic':
						return '<=50K'
					elif obj[13] == 'Peru':
						return '<=50K'
					elif obj[13] == 'Greece':
						return '<=50K'
					elif obj[13] == 'Scotland':
						return '<=50K'
					elif obj[13] == 'Portugal':
						return '<=50K'
					else: return '<=50K'
				else: return '<=50K'
			elif obj[5] == 'Separated':
				# {"feature": "capital-loss", "instances": 995, "metric_value": 0.2478, "depth": 4}
				if float(obj[11])<=1167.3293745933918:
					# {"feature": "hours-per-week", "instances": 970, "metric_value": 0.224, "depth": 5}
					if float(obj[12])<=49.53672262327997:
						# {"feature": "sex", "instances": 855, "metric_value": 0.1786, "depth": 6}
						if obj[9] == 'Female':
							# {"feature": "age", "instances": 555, "metric_value": 0.0861, "depth": 7}
							if float(obj[0])<=61.48868037271776:
								# {"feature": "workclass", "instances": 537, "metric_value": 0.0634, "depth": 8}
								if obj[1] == 'Private':
									# {"feature": "native-country", "instances": 461, "metric_value": 0.0566, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "education", "instances": 395, "metric_value": 0.0459, "depth": 10}
										if obj[3] == 'HS-grad':
											return '<=50K'
										elif obj[3] == 'Some-college':
											# {"feature": "relationship", "instances": 85, "metric_value": 0.0923, "depth": 11}
											if obj[7] == 'Unmarried':
												return '<=50K'
											elif obj[7] == 'Not-in-family':
												# {"feature": "fnlwgt", "instances": 18, "metric_value": 0.3095, "depth": 12}
												if float(obj[2])<=184945:
													return '<=50K'
												elif float(obj[2])>184945:
													# {"feature": "occupation", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[6] == 'Adm-clerical':
														return '<=50K'
													elif obj[6] == 'Sales':
														return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Exec-managerial':
														return '>50K'
													elif obj[6] == 'Tech-support':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											elif obj[7] == 'Own-child':
												return '<=50K'
											else: return '<=50K'
										elif obj[3] == '10th':
											return '<=50K'
										elif obj[3] == 'Bachelors':
											# {"feature": "fnlwgt", "instances": 20, "metric_value": 0.2864, "depth": 11}
											if float(obj[2])>118486:
												return '<=50K'
											elif float(obj[2])<=118486:
												# {"feature": "occupation", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[6] == 'Exec-managerial':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7] == 'Unmarried':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Tech-support':
													return '<=50K'
												elif obj[6] == 'Adm-clerical':
													return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[3] == '11th':
											return '<=50K'
										elif obj[3] == 'Assoc-voc':
											return '<=50K'
										elif obj[3] == '7th-8th':
											return '<=50K'
										elif obj[3] == 'Assoc-acdm':
											return '<=50K'
										elif obj[3] == '12th':
											return '<=50K'
										elif obj[3] == '9th':
											return '<=50K'
										elif obj[3] == 'Masters':
											return '<=50K'
										elif obj[3] == '5th-6th':
											return '<=50K'
										elif obj[3] == '1st-4th':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Mexico':
										return '<=50K'
									elif obj[13] == 'Puerto-Rico':
										return '<=50K'
									elif obj[13] == 'Philippines':
										# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'Adm-clerical':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 11}
											if float(obj[2])<=165235:
												return '>50K'
											elif float(obj[2])>165235:
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Jamaica':
										return '<=50K'
									elif obj[13] == 'El-Salvador':
										return '<=50K'
									elif obj[13] == 'Guatemala':
										return '<=50K'
									elif obj[13] == 'Dominican-Republic':
										return '<=50K'
									elif obj[13] == 'Columbia':
										return '<=50K'
									elif obj[13] == 'Cuba':
										return '<=50K'
									elif obj[13] == 'Germany':
										return '<=50K'
									elif obj[13] == 'Peru':
										return '<=50K'
									elif obj[13] == 'China':
										return '<=50K'
									elif obj[13] == 'Italy':
										return '<=50K'
									elif obj[13] == 'Haiti':
										return '<=50K'
									elif obj[13] == 'Japan':
										return '<=50K'
									elif obj[13] == 'Trinadad&Tobago':
										return '<=50K'
									elif obj[13] == 'Scotland':
										return '<=50K'
									elif obj[13] == 'Ireland':
										return '<=50K'
									elif obj[13] == 'India':
										return '<=50K'
									elif obj[13] == 'Canada':
										return '<=50K'
									else: return '<=50K'
								elif obj[1] == 'Local-gov':
									return '<=50K'
								elif obj[1] == 'State-gov':
									return '<=50K'
								elif obj[1] == 'Self-emp-not-inc':
									return '<=50K'
								elif obj[1] == 'Federal-gov':
									return '<=50K'
								elif obj[1] == 'Self-emp-inc':
									# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6] == 'Sales':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '>50K'
									else: return '>50K'
								else: return '<=50K'
							elif float(obj[0])>61.48868037271776:
								# {"feature": "workclass", "instances": 18, "metric_value": 0.5033, "depth": 8}
								if obj[1] == 'Private':
									# {"feature": "fnlwgt", "instances": 16, "metric_value": 0.3373, "depth": 9}
									if float(obj[2])<=298070:
										return '<=50K'
									elif float(obj[2])>298070:
										# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3] == 'Masters':
											return '>50K'
										elif obj[3] == '11th':
											return '<=50K'
										else: return '<=50K'
									else: return '>50K'
								elif obj[1] == 'Federal-gov':
									return '>50K'
								elif obj[1] == 'State-gov':
									return '<=50K'
								else: return '<=50K'
							else: return '<=50K'
						elif obj[9] == 'Male':
							# {"feature": "education", "instances": 300, "metric_value": 0.3141, "depth": 7}
							if obj[3] == 'HS-grad':
								# {"feature": "fnlwgt", "instances": 113, "metric_value": 0.1768, "depth": 8}
								if float(obj[2])<=569028.4339380782:
									# {"feature": "age", "instances": 111, "metric_value": 0.1302, "depth": 9}
									if float(obj[0])<=57.35067341798647:
										# {"feature": "occupation", "instances": 108, "metric_value": 0.0758, "depth": 10}
										if obj[6] == 'Craft-repair':
											return '<=50K'
										elif obj[6] == 'Machine-op-inspct':
											return '<=50K'
										elif obj[6] == 'Transport-moving':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '<=50K'
										elif obj[6] == 'Handlers-cleaners':
											return '<=50K'
										elif obj[6] == 'Adm-clerical':
											# {"feature": "relationship", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[7] == 'Not-in-family':
												# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "race", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "native-country", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														elif obj[13] == 'Columbia':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[1] == 'Self-emp-inc':
													return '<=50K'
												else: return '<=50K'
											elif obj[7] == 'Unmarried':
												return '<=50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											else: return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '<=50K'
										elif obj[6] == 'Protective-serv':
											return '<=50K'
										elif obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Farming-fishing':
											return '<=50K'
										elif obj[6] == 'Tech-support':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[0])>57.35067341798647:
										# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7] == 'Not-in-family':
											return '<=50K'
										elif obj[7] == 'Unmarried':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif float(obj[2])>569028.4339380782:
									# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if float(obj[0])<=34:
										return '>50K'
									elif float(obj[0])>34:
										return '<=50K'
									else: return '<=50K'
								else: return '>50K'
							elif obj[3] == 'Some-college':
								# {"feature": "occupation", "instances": 63, "metric_value": 0.3412, "depth": 8}
								if obj[6] == 'Craft-repair':
									# {"feature": "relationship", "instances": 13, "metric_value": 0.3912, "depth": 9}
									if obj[7] == 'Not-in-family':
										return '<=50K'
									elif obj[7] == 'Unmarried':
										return '>50K'
									elif obj[7] == 'Own-child':
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Adm-clerical':
									return '<=50K'
								elif obj[6] == 'Sales':
									return '<=50K'
								elif obj[6] == 'Handlers-cleaners':
									return '<=50K'
								elif obj[6] == 'Exec-managerial':
									# {"feature": "age", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if float(obj[0])<=40:
										return '<=50K'
									elif float(obj[0])>40:
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Other-service':
									return '<=50K'
								elif obj[6] == 'Machine-op-inspct':
									return '<=50K'
								elif obj[6] == 'Prof-specialty':
									return '<=50K'
								elif obj[6] == 'Tech-support':
									# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if float(obj[0])<=28:
										return '>50K'
									elif float(obj[0])>28:
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Protective-serv':
									# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if float(obj[0])<=52:
										return '<=50K'
									elif float(obj[0])>52:
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Transport-moving':
									return '<=50K'
								elif obj[6] == 'Farming-fishing':
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Bachelors':
								# {"feature": "fnlwgt", "instances": 33, "metric_value": 0.6136, "depth": 8}
								if float(obj[2])<=403193.1976372998:
									# {"feature": "native-country", "instances": 32, "metric_value": 0.5436, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "age", "instances": 30, "metric_value": 0.469, "depth": 10}
										if float(obj[0])<=46:
											return '<=50K'
										elif float(obj[0])>46:
											# {"feature": "workclass", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[6] == 'Sales':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[6] == 'Craft-repair':
													return '<=50K'
												elif obj[6] == 'Prof-specialty':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == 'Prof-specialty':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-inc':
												return '<=50K'
											elif obj[1] == 'Federal-gov':
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[13] == 'Philippines':
										# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if float(obj[0])<=27:
											return '>50K'
										elif float(obj[0])>27:
											return '<=50K'
										else: return '<=50K'
									else: return '>50K'
								elif float(obj[2])>403193.1976372998:
									return '>50K'
								else: return '>50K'
							elif obj[3] == '11th':
								return '<=50K'
							elif obj[3] == '9th':
								return '<=50K'
							elif obj[3] == '10th':
								# {"feature": "race", "instances": 14, "metric_value": 0.3712, "depth": 8}
								if obj[8] == 'White':
									return '<=50K'
								elif obj[8] == 'Black':
									# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if float(obj[0])<=54:
										return '>50K'
									elif float(obj[0])>54:
										return '<=50K'
									else: return '<=50K'
								else: return '>50K'
							elif obj[3] == 'Assoc-voc':
								# {"feature": "relationship", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[7] == 'Not-in-family':
									return '<=50K'
								elif obj[7] == 'Other-relative':
									return '>50K'
								else: return '>50K'
							elif obj[3] == '7th-8th':
								return '<=50K'
							elif obj[3] == 'Assoc-acdm':
								return '<=50K'
							elif obj[3] == '5th-6th':
								return '<=50K'
							elif obj[3] == 'Masters':
								# {"feature": "age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if float(obj[0])<=42:
									return '>50K'
								elif float(obj[0])>42:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == '1st-4th':
								return '<=50K'
							elif obj[3] == '12th':
								return '<=50K'
							else: return '<=50K'
						else: return '<=50K'
					elif float(obj[12])>49.53672262327997:
						# {"feature": "native-country", "instances": 115, "metric_value": 0.4826, "depth": 6}
						if obj[13] == 'United-States':
							# {"feature": "race", "instances": 99, "metric_value": 0.5033, "depth": 7}
							if obj[8] == 'White':
								# {"feature": "age", "instances": 84, "metric_value": 0.56, "depth": 8}
								if float(obj[0])<=59.148571031141245:
									# {"feature": "education", "instances": 81, "metric_value": 0.5731, "depth": 9}
									if obj[3] == 'HS-grad':
										# {"feature": "workclass", "instances": 25, "metric_value": 0.2423, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										elif obj[1] == 'Local-gov':
											return '<=50K'
										else: return '<=50K'
									elif obj[3] == 'Some-college':
										# {"feature": "fnlwgt", "instances": 22, "metric_value": 0.7732, "depth": 10}
										if float(obj[2])>29874:
											# {"feature": "occupation", "instances": 21, "metric_value": 0.7025, "depth": 11}
											if obj[6] == 'Sales':
												# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[1] == 'Self-emp-not-inc':
													return '<=50K'
												elif obj[1] == 'Private':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Other-service':
												return '<=50K'
											elif obj[6] == 'Adm-clerical':
												# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1] == 'Private':
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Own-child':
														return '<=50K'
													elif obj[7] == 'Unmarried':
														return '>50K'
													else: return '>50K'
												elif obj[1] == 'State-gov':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Exec-managerial':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Unmarried':
													return '<=50K'
												elif obj[7] == 'Not-in-family':
													return '>50K'
												else: return '>50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											elif obj[6] == 'Protective-serv':
												return '<=50K'
											elif obj[6] == 'Farming-fishing':
												return '<=50K'
											elif obj[6] == 'Transport-moving':
												return '>50K'
											elif obj[6] == 'Tech-support':
												return '<=50K'
											else: return '<=50K'
										elif float(obj[2])<=29874:
											return '>50K'
										else: return '>50K'
									elif obj[3] == 'Bachelors':
										# {"feature": "fnlwgt", "instances": 17, "metric_value": 0.7871, "depth": 10}
										if float(obj[2])>27766:
											# {"feature": "sex", "instances": 16, "metric_value": 0.6962, "depth": 11}
											if obj[9] == 'Female':
												# {"feature": "relationship", "instances": 10, "metric_value": 0.8813, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "occupation", "instances": 8, "metric_value": 0.9544, "depth": 13}
													if obj[6] == 'Prof-specialty':
														# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[1] == 'Local-gov':
															return '>50K'
														elif obj[1] == 'Self-emp-inc':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													elif obj[6] == 'Sales':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												else: return '<=50K'
											elif obj[9] == 'Male':
												return '<=50K'
											else: return '<=50K'
										elif float(obj[2])<=27766:
											return '>50K'
										else: return '>50K'
									elif obj[3] == 'Assoc-acdm':
										return '<=50K'
									elif obj[3] == 'Masters':
										# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6] == 'Prof-specialty':
											return '<=50K'
										elif obj[6] == 'Exec-managerial':
											return '>50K'
										else: return '>50K'
									elif obj[3] == '11th':
										return '<=50K'
									elif obj[3] == '10th':
										return '<=50K'
									elif obj[3] == 'Assoc-voc':
										return '<=50K'
									elif obj[3] == '9th':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[0])>59.148571031141245:
									return '<=50K'
								else: return '<=50K'
							elif obj[8] == 'Black':
								return '<=50K'
							elif obj[8] == 'Other':
								return '<=50K'
							else: return '<=50K'
						elif obj[13] == 'Mexico':
							return '<=50K'
						elif obj[13] == 'Germany':
							return '<=50K'
						elif obj[13] == 'Puerto-Rico':
							return '<=50K'
						elif obj[13] == 'England':
							return '<=50K'
						elif obj[13] == 'Philippines':
							return '<=50K'
						elif obj[13] == 'Portugal':
							return '>50K'
						elif obj[13] == 'Canada':
							return '<=50K'
						elif obj[13] == 'Peru':
							return '<=50K'
						elif obj[13] == 'Columbia':
							return '<=50K'
						elif obj[13] == 'Japan':
							return '<=50K'
						elif obj[13] == 'South':
							return '<=50K'
						else: return '<=50K'
					else: return '<=50K'
				elif float(obj[11])>1167.3293745933918:
					# {"feature": "age", "instances": 25, "metric_value": 0.795, "depth": 5}
					if float(obj[0])>23:
						# {"feature": "hours-per-week", "instances": 24, "metric_value": 0.7383, "depth": 6}
						if float(obj[12])<=40:
							return '<=50K'
						elif float(obj[12])>40:
							# {"feature": "fnlwgt", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if float(obj[2])>77009:
								# {"feature": "native-country", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[13] == 'United-States':
									# {"feature": "education", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[3] == 'Some-college':
										# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6] == 'Craft-repair':
											# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[6] == 'Machine-op-inspct':
											return '>50K'
										else: return '>50K'
									elif obj[3] == 'Masters':
										return '>50K'
									elif obj[3] == 'Bachelors':
										return '>50K'
									elif obj[3] == 'Assoc-voc':
										return '>50K'
									else: return '>50K'
								elif obj[13] == 'England':
									return '<=50K'
								else: return '<=50K'
							elif float(obj[2])<=77009:
								return '<=50K'
							else: return '<=50K'
						else: return '>50K'
					elif float(obj[0])<=23:
						return '>50K'
					else: return '>50K'
				else: return '<=50K'
			elif obj[5] == 'Widowed':
				# {"feature": "hours-per-week", "instances": 962, "metric_value": 0.3449, "depth": 4}
				if float(obj[12])<=46.714729672704046:
					# {"feature": "sex", "instances": 882, "metric_value": 0.2907, "depth": 5}
					if obj[9] == 'Female':
						# {"feature": "capital-loss", "instances": 751, "metric_value": 0.2171, "depth": 6}
						if float(obj[11])<=2238:
							# {"feature": "native-country", "instances": 745, "metric_value": 0.2054, "depth": 7}
							if obj[13] == 'United-States':
								# {"feature": "occupation", "instances": 686, "metric_value": 0.2118, "depth": 8}
								if obj[6] == 'Prof-specialty':
									# {"feature": "education", "instances": 171, "metric_value": 0.2193, "depth": 9}
									if obj[3] == 'HS-grad':
										# {"feature": "fnlwgt", "instances": 61, "metric_value": 0.1207, "depth": 10}
										if float(obj[2])<=158525.83606557376:
											# {"feature": "age", "instances": 32, "metric_value": 0.2006, "depth": 11}
											if float(obj[0])>64.625:
												# {"feature": "relationship", "instances": 19, "metric_value": 0.2975, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 13, "metric_value": 0.3912, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "workclass", "instances": 11, "metric_value": 0.4395, "depth": 14}
														if obj[1] == 'Private':
															return '<=50K'
														else: return '<=50K'
													elif obj[8] == 'Black':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[0])<=64.625:
												return '<=50K'
											else: return '<=50K'
										elif float(obj[2])>158525.83606557376:
											return '<=50K'
										else: return '<=50K'
									elif obj[3] == 'Some-college':
										return '<=50K'
									elif obj[3] == 'Assoc-voc':
										return '<=50K'
									elif obj[3] == 'Masters':
										# {"feature": "age", "instances": 19, "metric_value": 0.4855, "depth": 10}
										if float(obj[0])<=59:
											return '<=50K'
										elif float(obj[0])>59:
											# {"feature": "race", "instances": 9, "metric_value": 0.7642, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "fnlwgt", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if float(obj[2])>99784:
													return '<=50K'
												elif float(obj[2])<=99784:
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '>50K'
														else: return '>50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[3] == 'Bachelors':
										# {"feature": "age", "instances": 18, "metric_value": 0.65, "depth": 10}
										if float(obj[0])>35:
											# {"feature": "fnlwgt", "instances": 17, "metric_value": 0.5226, "depth": 11}
											if float(obj[2])>31365:
												# {"feature": "relationship", "instances": 16, "metric_value": 0.3373, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "workclass", "instances": 10, "metric_value": 0.469, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														elif obj[8] == 'Other':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Local-gov':
														return '<=50K'
													elif obj[1] == 'State-gov':
														return '<=50K'
													elif obj[1] == 'Federal-gov':
														return '<=50K'
													else: return '<=50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												elif obj[7] == 'Other-relative':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])<=31365:
												return '>50K'
											else: return '>50K'
										elif float(obj[0])<=35:
											return '>50K'
										else: return '>50K'
									elif obj[3] == '7th-8th':
										return '<=50K'
									elif obj[3] == '11th':
										return '<=50K'
									elif obj[3] == 'Assoc-acdm':
										return '<=50K'
									elif obj[3] == '5th-6th':
										return '<=50K'
									elif obj[3] == '9th':
										return '<=50K'
									elif obj[3] == '10th':
										return '<=50K'
									elif obj[3] == '1st-4th':
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Adm-clerical':
									# {"feature": "workclass", "instances": 141, "metric_value": 0.1074, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "age", "instances": 103, "metric_value": 0.0789, "depth": 10}
										if float(obj[0])>56.83495145631068:
											# {"feature": "fnlwgt", "instances": 57, "metric_value": 0.1274, "depth": 11}
											if float(obj[2])<=176516.9649122807:
												# {"feature": "education", "instances": 31, "metric_value": 0.2056, "depth": 12}
												if obj[3] == 'HS-grad':
													# {"feature": "relationship", "instances": 18, "metric_value": 0.3095, "depth": 13}
													if obj[7] == 'Not-in-family':
														# {"feature": "race", "instances": 13, "metric_value": 0.3912, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													else: return '<=50K'
												elif obj[3] == 'Some-college':
													return '<=50K'
												elif obj[3] == 'Assoc-voc':
													return '<=50K'
												elif obj[3] == '10th':
													return '<=50K'
												elif obj[3] == '11th':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])>176516.9649122807:
												return '<=50K'
											else: return '<=50K'
										elif float(obj[0])<=56.83495145631068:
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Local-gov':
										# {"feature": "relationship", "instances": 18, "metric_value": 0.3095, "depth": 10}
										if obj[7] == 'Not-in-family':
											return '<=50K'
										elif obj[7] == 'Unmarried':
											# {"feature": "age", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if float(obj[0])<=61:
												return '<=50K'
											elif float(obj[0])>61:
												# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 12}
												if float(obj[2])<=75134:
													return '<=50K'
												elif float(obj[2])>75134:
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Federal-gov':
										return '<=50K'
									elif obj[1] == 'State-gov':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Other-service':
									# {"feature": "workclass", "instances": 138, "metric_value": 0.0619, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'Local-gov':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									elif obj[1] == 'State-gov':
										# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[7] == 'Not-in-family':
											return '<=50K'
										elif obj[7] == 'Unmarried':
											return '>50K'
										elif obj[7] == 'Other-relative':
											return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'Federal-gov':
										return '<=50K'
									elif obj[1] == 'Self-emp-inc':
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Sales':
									# {"feature": "age", "instances": 70, "metric_value": 0.3712, "depth": 9}
									if float(obj[0])>35.906211045149426:
										# {"feature": "relationship", "instances": 67, "metric_value": 0.3263, "depth": 10}
										if obj[7] == 'Not-in-family':
											# {"feature": "fnlwgt", "instances": 38, "metric_value": 0.4855, "depth": 11}
											if float(obj[2])<=263780.31318078504:
												# {"feature": "education", "instances": 31, "metric_value": 0.5548, "depth": 12}
												if obj[3] == 'HS-grad':
													# {"feature": "workclass", "instances": 14, "metric_value": 0.7496, "depth": 13}
													if obj[1] == 'Private':
														# {"feature": "race", "instances": 13, "metric_value": 0.7793, "depth": 14}
														if obj[8] == 'White':
															return '<=50K'
														else: return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														return '<=50K'
													else: return '<=50K'
												elif obj[3] == 'Some-college':
													# {"feature": "workclass", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[1] == 'Private':
														return '<=50K'
													elif obj[1] == 'Self-emp-inc':
														# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == 'White':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[3] == 'Masters':
													return '<=50K'
												elif obj[3] == '10th':
													return '<=50K'
												elif obj[3] == '12th':
													return '<=50K'
												elif obj[3] == '9th':
													return '<=50K'
												elif obj[3] == '11th':
													return '<=50K'
												elif obj[3] == 'Assoc-voc':
													return '<=50K'
												else: return '<=50K'
											elif float(obj[2])>263780.31318078504:
												return '<=50K'
											else: return '<=50K'
										elif obj[7] == 'Unmarried':
											return '<=50K'
										elif obj[7] == 'Other-relative':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[0])<=35.906211045149426:
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif obj[6] == 'Exec-managerial':
									# {"feature": "race", "instances": 55, "metric_value": 0.5983, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "fnlwgt", "instances": 44, "metric_value": 0.6321, "depth": 10}
										if float(obj[2])>23074:
											# {"feature": "education", "instances": 43, "metric_value": 0.583, "depth": 11}
											if obj[3] == 'HS-grad':
												# {"feature": "age", "instances": 15, "metric_value": 0.3534, "depth": 12}
												if float(obj[0])<=66:
													return '<=50K'
												elif float(obj[0])>66:
													# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[1] == 'Local-gov':
														return '<=50K'
													elif obj[1] == 'Private':
														# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7] == 'Not-in-family':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[3] == 'Some-college':
												# {"feature": "age", "instances": 11, "metric_value": 0.4395, "depth": 12}
												if float(obj[0])>38:
													return '<=50K'
												elif float(obj[0])<=38:
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Unmarried':
														return '<=50K'
													elif obj[7] == 'Not-in-family':
														return '>50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[3] == 'Assoc-voc':
												return '<=50K'
											elif obj[3] == 'Bachelors':
												# {"feature": "workclass", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[1] == 'Private':
													return '<=50K'
												elif obj[1] == 'Federal-gov':
													return '>50K'
												else: return '>50K'
											elif obj[3] == 'Assoc-acdm':
												# {"feature": "age", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if float(obj[0])>35:
													# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == 'Not-in-family':
														return '>50K'
													elif obj[7] == 'Unmarried':
														return '<=50K'
													else: return '<=50K'
												elif float(obj[0])<=35:
													return '<=50K'
												else: return '<=50K'
											elif obj[3] == 'Masters':
												return '>50K'
											elif obj[3] == '11th':
												return '<=50K'
											elif obj[3] == '12th':
												return '<=50K'
											else: return '<=50K'
										elif float(obj[2])<=23074:
											return '>50K'
										else: return '>50K'
									elif obj[8] == 'Black':
										return '<=50K'
									elif obj[8] == 'Amer-Indian-Eskimo':
										return '<=50K'
									elif obj[8] == 'Asian-Pac-Islander':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Machine-op-inspct':
									return '<=50K'
								elif obj[6] == 'Tech-support':
									# {"feature": "age", "instances": 16, "metric_value": 0.3373, "depth": 9}
									if float(obj[0])>45:
										return '<=50K'
									elif float(obj[0])<=45:
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Federal-gov':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif obj[6] == 'Craft-repair':
									return '<=50K'
								elif obj[6] == 'Priv-house-serv':
									return '<=50K'
								elif obj[6] == 'Handlers-cleaners':
									return '<=50K'
								elif obj[6] == 'Transport-moving':
									return '<=50K'
								elif obj[6] == 'Farming-fishing':
									return '<=50K'
								elif obj[6] == 'Protective-serv':
									return '<=50K'
								else: return '<=50K'
							elif obj[13] == 'Mexico':
								return '<=50K'
							elif obj[13] == 'Cuba':
								return '<=50K'
							elif obj[13] == 'Germany':
								return '<=50K'
							elif obj[13] == 'Puerto-Rico':
								return '<=50K'
							elif obj[13] == 'Italy':
								return '<=50K'
							elif obj[13] == 'Philippines':
								return '<=50K'
							elif obj[13] == 'El-Salvador':
								return '<=50K'
							elif obj[13] == 'Canada':
								return '<=50K'
							elif obj[13] == 'England':
								return '<=50K'
							elif obj[13] == 'Portugal':
								return '<=50K'
							elif obj[13] == 'Haiti':
								return '<=50K'
							elif obj[13] == 'Hungary':
								return '<=50K'
							elif obj[13] == 'Guatemala':
								return '<=50K'
							elif obj[13] == 'Columbia':
								return '<=50K'
							elif obj[13] == 'Poland':
								return '<=50K'
							elif obj[13] == 'Nicaragua':
								return '<=50K'
							elif obj[13] == 'India':
								# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if float(obj[0])>36:
									return '>50K'
								elif float(obj[0])<=36:
									return '<=50K'
								else: return '<=50K'
							elif obj[13] == 'Thailand':
								return '<=50K'
							elif obj[13] == 'China':
								return '<=50K'
							elif obj[13] == 'South':
								return '<=50K'
							elif obj[13] == 'Dominican-Republic':
								return '<=50K'
							elif obj[13] == 'Ecuador':
								return '<=50K'
							elif obj[13] == 'Japan':
								return '<=50K'
							elif obj[13] == 'Jamaica':
								return '<=50K'
							elif obj[13] == 'Outlying-US(Guam-USVI-etc)':
								return '<=50K'
							else: return '<=50K'
						elif float(obj[11])>2238:
							# {"feature": "occupation", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6] == 'Prof-specialty':
								return '<=50K'
							elif obj[6] == 'Other-service':
								return '>50K'
							elif obj[6] == 'Exec-managerial':
								return '<=50K'
							elif obj[6] == 'Adm-clerical':
								return '>50K'
							else: return '>50K'
						else: return '<=50K'
					elif obj[9] == 'Male':
						# {"feature": "capital-loss", "instances": 131, "metric_value": 0.5973, "depth": 6}
						if float(obj[11])<=2339:
							# {"feature": "workclass", "instances": 130, "metric_value": 0.5802, "depth": 7}
							if obj[1] == 'Private':
								# {"feature": "age", "instances": 87, "metric_value": 0.5146, "depth": 8}
								if float(obj[0])<=75.8557122149906:
									# {"feature": "occupation", "instances": 71, "metric_value": 0.5864, "depth": 9}
									if obj[6] == 'Prof-specialty':
										# {"feature": "fnlwgt", "instances": 14, "metric_value": 0.3712, "depth": 10}
										if float(obj[2])<=195981:
											return '<=50K'
										elif float(obj[2])>195981:
											# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == 'HS-grad':
												return '<=50K'
											elif obj[3] == 'Bachelors':
												return '>50K'
											else: return '>50K'
										else: return '<=50K'
									elif obj[6] == 'Craft-repair':
										# {"feature": "fnlwgt", "instances": 12, "metric_value": 0.4138, "depth": 10}
										if float(obj[2])>99185:
											return '<=50K'
										elif float(obj[2])<=99185:
											# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Unmarried':
												return '>50K'
											elif obj[7] == 'Not-in-family':
												return '<=50K'
											else: return '<=50K'
										else: return '>50K'
									elif obj[6] == 'Transport-moving':
										# {"feature": "fnlwgt", "instances": 10, "metric_value": 0.7219, "depth": 10}
										if float(obj[2])>34269:
											# {"feature": "education", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[3] == 'HS-grad':
												return '<=50K'
											elif obj[3] == '7th-8th':
												return '<=50K'
											elif obj[3] == '11th':
												return '<=50K'
											elif obj[3] == '10th':
												return '<=50K'
											elif obj[3] == '9th':
												return '>50K'
											else: return '>50K'
										elif float(obj[2])<=34269:
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Sales':
										# {"feature": "fnlwgt", "instances": 5, "metric_value": 0.971, "depth": 10}
										if float(obj[2])>113324:
											# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == 'Some-college':
												return '>50K'
											elif obj[3] == 'Bachelors':
												return '>50K'
											elif obj[3] == 'HS-grad':
												return '<=50K'
											else: return '<=50K'
										elif float(obj[2])<=113324:
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Exec-managerial':
										# {"feature": "fnlwgt", "instances": 5, "metric_value": 0.971, "depth": 10}
										if float(obj[2])<=196610:
											# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[7] == 'Unmarried':
												return '>50K'
											elif obj[7] == 'Other-relative':
												return '<=50K'
											elif obj[7] == 'Not-in-family':
												return '>50K'
											else: return '>50K'
										elif float(obj[2])>196610:
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Farming-fishing':
										return '<=50K'
									elif obj[6] == 'Adm-clerical':
										return '<=50K'
									elif obj[6] == 'Handlers-cleaners':
										return '<=50K'
									elif obj[6] == 'Tech-support':
										# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 10}
										if float(obj[2])<=122493:
											return '<=50K'
										elif float(obj[2])>122493:
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif float(obj[0])>75.8557122149906:
									return '<=50K'
								else: return '<=50K'
							elif obj[1] == 'Self-emp-not-inc':
								return '<=50K'
							elif obj[1] == 'Local-gov':
								# {"feature": "fnlwgt", "instances": 13, "metric_value": 0.7793, "depth": 8}
								if float(obj[2])<=303860:
									# {"feature": "age", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if float(obj[0])>49:
										return '<=50K'
									elif float(obj[0])<=49:
										# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3] == 'HS-grad':
											return '<=50K'
										elif obj[3] == 'Assoc-acdm':
											return '<=50K'
										elif obj[3] == '9th':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif float(obj[2])>303860:
									return '>50K'
								else: return '>50K'
							elif obj[1] == 'Self-emp-inc':
								# {"feature": "fnlwgt", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if float(obj[2])>98116:
									# {"feature": "age", "instances": 5, "metric_value": 0.971, "depth": 9}
									if float(obj[0])>53:
										# {"feature": "education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3] == 'Some-college':
											return '<=50K'
										elif obj[3] == '10th':
											return '<=50K'
										elif obj[3] == 'HS-grad':
											return '>50K'
										else: return '>50K'
									elif float(obj[0])<=53:
										return '>50K'
									else: return '>50K'
								elif float(obj[2])<=98116:
									return '>50K'
								else: return '>50K'
							elif obj[1] == 'Federal-gov':
								# {"feature": "age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if float(obj[0])>35:
									return '<=50K'
								elif float(obj[0])<=35:
									return '>50K'
								else: return '>50K'
							elif obj[1] == 'State-gov':
								return '<=50K'
							else: return '<=50K'
						elif float(obj[11])>2339:
							return '>50K'
						else: return '>50K'
					else: return '<=50K'
				elif float(obj[12])>46.714729672704046:
					# {"feature": "capital-loss", "instances": 80, "metric_value": 0.7462, "depth": 5}
					if float(obj[11])<=1669:
						# {"feature": "native-country", "instances": 77, "metric_value": 0.684, "depth": 6}
						if obj[13] == 'United-States':
							# {"feature": "age", "instances": 70, "metric_value": 0.6274, "depth": 7}
							if float(obj[0])>30.69127746385058:
								# {"feature": "occupation", "instances": 68, "metric_value": 0.6024, "depth": 8}
								if obj[6] == 'Prof-specialty':
									# {"feature": "workclass", "instances": 15, "metric_value": 0.8366, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'Local-gov':
										# {"feature": "fnlwgt", "instances": 5, "metric_value": 0.971, "depth": 10}
										if float(obj[2])<=291175:
											# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[7] == 'Not-in-family':
												return '<=50K'
											elif obj[7] == 'Unmarried':
												# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3] == 'Masters':
													return '<=50K'
												elif obj[3] == 'Bachelors':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif float(obj[2])>291175:
											return '>50K'
										else: return '>50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Exec-managerial':
									# {"feature": "sex", "instances": 13, "metric_value": 0.3912, "depth": 9}
									if obj[9] == 'Female':
										return '<=50K'
									elif obj[9] == 'Male':
										# {"feature": "relationship", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[7] == 'Not-in-family':
											return '<=50K'
										elif obj[7] == 'Unmarried':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif obj[6] == 'Sales':
									# {"feature": "fnlwgt", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if float(obj[2])>28612:
										# {"feature": "race", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "relationship", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[7] == 'Unmarried':
												return '>50K'
											elif obj[7] == 'Not-in-family':
												# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[9] == 'Female':
													return '<=50K'
												elif obj[9] == 'Male':
													return '>50K'
												else: return '>50K'
											else: return '<=50K'
										elif obj[8] == 'Black':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[2])<=28612:
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Farming-fishing':
									return '<=50K'
								elif obj[6] == 'Other-service':
									return '<=50K'
								elif obj[6] == 'Adm-clerical':
									return '<=50K'
								elif obj[6] == 'Machine-op-inspct':
									return '<=50K'
								elif obj[6] == 'Craft-repair':
									# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Transport-moving':
									return '<=50K'
								elif obj[6] == 'Priv-house-serv':
									return '<=50K'
								elif obj[6] == 'Handlers-cleaners':
									return '<=50K'
								elif obj[6] == 'Protective-serv':
									return '<=50K'
								else: return '<=50K'
							elif float(obj[0])<=30.69127746385058:
								# {"feature": "fnlwgt", "instances": 2, "metric_value": 1.0, "depth": 8}
								if float(obj[2])>67257:
									return '>50K'
								elif float(obj[2])<=67257:
									return '<=50K'
								else: return '<=50K'
							else: return '>50K'
						elif obj[13] == 'South':
							return '<=50K'
						elif obj[13] == 'England':
							return '<=50K'
						elif obj[13] == 'Poland':
							return '>50K'
						elif obj[13] == 'Greece':
							return '>50K'
						elif obj[13] == 'Thailand':
							return '<=50K'
						elif obj[13] == 'El-Salvador':
							return '>50K'
						else: return '>50K'
					elif float(obj[11])>1669:
						return '>50K'
					else: return '>50K'
				else: return '<=50K'
			elif obj[5] == 'Married-spouse-absent':
				# {"feature": "capital-loss", "instances": 403, "metric_value": 0.3355, "depth": 4}
				if float(obj[11])<=2339:
					# {"feature": "hours-per-week", "instances": 402, "metric_value": 0.3263, "depth": 5}
					if float(obj[12])<=51.10099343363879:
						# {"feature": "workclass", "instances": 369, "metric_value": 0.2812, "depth": 6}
						if obj[1] == 'Private':
							# {"feature": "age", "instances": 298, "metric_value": 0.2435, "depth": 7}
							if float(obj[0])<=39.26845637583892:
								# {"feature": "fnlwgt", "instances": 157, "metric_value": 0.0984, "depth": 8}
								if float(obj[2])>64339.470591962396:
									# {"feature": "education", "instances": 140, "metric_value": 0.0612, "depth": 9}
									if obj[3] == 'HS-grad':
										return '<=50K'
									elif obj[3] == 'Some-college':
										return '<=50K'
									elif obj[3] == 'Bachelors':
										# {"feature": "sex", "instances": 14, "metric_value": 0.3712, "depth": 10}
										if obj[9] == 'Female':
											return '<=50K'
										elif obj[9] == 'Male':
											# {"feature": "occupation", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[6] == 'Craft-repair':
												# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'Not-in-family':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Black':
														return '<=50K'
													elif obj[8] == 'White':
														return '>50K'
													else: return '>50K'
												elif obj[7] == 'Unmarried':
													return '<=50K'
												else: return '<=50K'
											elif obj[6] == 'Adm-clerical':
												return '<=50K'
											elif obj[6] == 'Prof-specialty':
												return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[3] == '11th':
										return '<=50K'
									elif obj[3] == '5th-6th':
										return '<=50K'
									elif obj[3] == '9th':
										return '<=50K'
									elif obj[3] == 'Assoc-acdm':
										return '<=50K'
									elif obj[3] == '1st-4th':
										return '<=50K'
									elif obj[3] == '10th':
										return '<=50K'
									elif obj[3] == '7th-8th':
										return '<=50K'
									elif obj[3] == 'Assoc-voc':
										return '<=50K'
									elif obj[3] == '12th':
										return '<=50K'
									elif obj[3] == 'Preschool':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[2])<=64339.470591962396:
									# {"feature": "occupation", "instances": 17, "metric_value": 0.3228, "depth": 9}
									if obj[6] == 'Other-service':
										return '<=50K'
									elif obj[6] == 'Prof-specialty':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										return '<=50K'
									elif obj[6] == 'Adm-clerical':
										return '<=50K'
									elif obj[6] == 'Protective-serv':
										return '<=50K'
									elif obj[6] == 'Exec-managerial':
										return '<=50K'
									elif obj[6] == 'Sales':
										return '<=50K'
									elif obj[6] == 'Transport-moving':
										return '<=50K'
									elif obj[6] == 'Craft-repair':
										return '>50K'
									else: return '>50K'
								else: return '<=50K'
							elif float(obj[0])>39.26845637583892:
								# {"feature": "relationship", "instances": 141, "metric_value": 0.3694, "depth": 8}
								if obj[7] == 'Not-in-family':
									# {"feature": "fnlwgt", "instances": 76, "metric_value": 0.5248, "depth": 9}
									if float(obj[2])>27444:
										# {"feature": "native-country", "instances": 75, "metric_value": 0.4898, "depth": 10}
										if obj[13] == 'United-States':
											# {"feature": "race", "instances": 42, "metric_value": 0.65, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "education", "instances": 38, "metric_value": 0.6892, "depth": 12}
												if obj[3] == 'Bachelors':
													# {"feature": "occupation", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[6] == 'Prof-specialty':
														# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[6] == 'Exec-managerial':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[6] == 'Other-service':
														return '<=50K'
													else: return '<=50K'
												elif obj[3] == 'HS-grad':
													# {"feature": "sex", "instances": 9, "metric_value": 0.7642, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "occupation", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[6] == 'Prof-specialty':
															return '<=50K'
														elif obj[6] == 'Craft-repair':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														return '<=50K'
													else: return '<=50K'
												elif obj[3] == 'Some-college':
													# {"feature": "occupation", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[6] == 'Adm-clerical':
														return '<=50K'
													elif obj[6] == 'Prof-specialty':
														return '<=50K'
													elif obj[6] == 'Transport-moving':
														return '<=50K'
													elif obj[6] == 'Machine-op-inspct':
														return '>50K'
													else: return '>50K'
												elif obj[3] == 'Masters':
													return '<=50K'
												elif obj[3] == 'Assoc-voc':
													return '<=50K'
												elif obj[3] == '7th-8th':
													return '<=50K'
												elif obj[3] == '1st-4th':
													return '<=50K'
												elif obj[3] == '5th-6th':
													return '<=50K'
												elif obj[3] == '12th':
													return '<=50K'
												elif obj[3] == 'Assoc-acdm':
													return '<=50K'
												elif obj[3] == '10th':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '<=50K'
											else: return '<=50K'
										elif obj[13] == 'Mexico':
											return '<=50K'
										elif obj[13] == 'Philippines':
											return '<=50K'
										elif obj[13] == 'China':
											return '<=50K'
										elif obj[13] == 'Columbia':
											return '<=50K'
										elif obj[13] == 'Jamaica':
											return '<=50K'
										elif obj[13] == 'Guatemala':
											return '<=50K'
										elif obj[13] == 'Poland':
											return '<=50K'
										elif obj[13] == 'Cuba':
											return '<=50K'
										elif obj[13] == 'Canada':
											return '<=50K'
										elif obj[13] == 'India':
											return '<=50K'
										elif obj[13] == 'Iran':
											return '<=50K'
										elif obj[13] == 'Japan':
											return '>50K'
										elif obj[13] == 'Puerto-Rico':
											return '<=50K'
										elif obj[13] == 'Dominican-Republic':
											return '<=50K'
										else: return '<=50K'
									elif float(obj[2])<=27444:
										return '>50K'
									else: return '>50K'
								elif obj[7] == 'Unmarried':
									return '<=50K'
								elif obj[7] == 'Other-relative':
									# {"feature": "sex", "instances": 12, "metric_value": 0.4138, "depth": 9}
									if obj[9] == 'Male':
										return '<=50K'
									elif obj[9] == 'Female':
										# {"feature": "fnlwgt", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if float(obj[2])<=101077:
											return '<=50K'
										elif float(obj[2])>101077:
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif obj[7] == 'Own-child':
									return '<=50K'
								else: return '<=50K'
							else: return '<=50K'
						elif obj[1] == 'Self-emp-not-inc':
							# {"feature": "age", "instances": 22, "metric_value": 0.7732, "depth": 7}
							if float(obj[0])<=75:
								# {"feature": "relationship", "instances": 21, "metric_value": 0.7025, "depth": 8}
								if obj[7] == 'Not-in-family':
									# {"feature": "fnlwgt", "instances": 15, "metric_value": 0.5665, "depth": 9}
									if float(obj[2])>133694:
										return '<=50K'
									elif float(obj[2])<=133694:
										# {"feature": "education", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[3] == 'Bachelors':
											return '>50K'
										elif obj[3] == 'HS-grad':
											return '<=50K'
										elif obj[3] == 'Masters':
											return '<=50K'
										elif obj[3] == '10th':
											return '<=50K'
										else: return '<=50K'
									else: return '<=50K'
								elif obj[7] == 'Unmarried':
									return '<=50K'
								elif obj[7] == 'Own-child':
									return '>50K'
								elif obj[7] == 'Other-relative':
									return '>50K'
								else: return '>50K'
							elif float(obj[0])>75:
								return '>50K'
							else: return '>50K'
						elif obj[1] == 'Local-gov':
							return '<=50K'
						elif obj[1] == 'State-gov':
							# {"feature": "age", "instances": 16, "metric_value": 0.3373, "depth": 7}
							if float(obj[0])<=50:
								return '<=50K'
							elif float(obj[0])>50:
								# {"feature": "fnlwgt", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if float(obj[2])>109600:
									return '<=50K'
								elif float(obj[2])<=109600:
									return '>50K'
								else: return '>50K'
							else: return '<=50K'
						elif obj[1] == 'Federal-gov':
							return '<=50K'
						elif obj[1] == 'Self-emp-inc':
							return '<=50K'
						elif obj[1] == 'Without-pay':
							return '<=50K'
						else: return '<=50K'
					elif float(obj[12])>51.10099343363879:
						# {"feature": "age", "instances": 33, "metric_value": 0.684, "depth": 6}
						if float(obj[0])<=64.22881288592602:
							# {"feature": "fnlwgt", "instances": 32, "metric_value": 0.6253, "depth": 7}
							if float(obj[2])>44257:
								# {"feature": "education", "instances": 31, "metric_value": 0.5548, "depth": 8}
								if obj[3] == 'HS-grad':
									# {"feature": "race", "instances": 14, "metric_value": 0.3712, "depth": 9}
									if obj[8] == 'White':
										return '<=50K'
									elif obj[8] == 'Black':
										# {"feature": "occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'Priv-house-serv':
											return '<=50K'
										elif obj[6] == 'Other-service':
											return '>50K'
										else: return '>50K'
									else: return '<=50K'
								elif obj[3] == 'Bachelors':
									return '<=50K'
								elif obj[3] == 'Masters':
									# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7] == 'Not-in-family':
										return '>50K'
									elif obj[7] == 'Other-relative':
										return '<=50K'
									else: return '<=50K'
								elif obj[3] == '12th':
									return '<=50K'
								elif obj[3] == '11th':
									return '<=50K'
								elif obj[3] == '10th':
									return '<=50K'
								elif obj[3] == '9th':
									return '<=50K'
								elif obj[3] == '1st-4th':
									return '<=50K'
								elif obj[3] == 'Assoc-acdm':
									return '<=50K'
								elif obj[3] == 'Some-college':
									return '>50K'
								else: return '>50K'
							elif float(obj[2])<=44257:
								return '>50K'
							else: return '>50K'
						elif float(obj[0])>64.22881288592602:
							return '>50K'
						else: return '>50K'
					else: return '<=50K'
				elif float(obj[11])>2339:
					return '>50K'
				else: return '>50K'
			elif obj[5] == 'Married-AF-spouse':
				# {"feature": "hours-per-week", "instances": 23, "metric_value": 0.9877, "depth": 4}
				if float(obj[12])>38:
					# {"feature": "age", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if float(obj[0])>19:
						# {"feature": "fnlwgt", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if float(obj[2])>30565:
							# {"feature": "education", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[3] == 'HS-grad':
								# {"feature": "relationship", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[7] == 'Husband':
									return '<=50K'
								elif obj[7] == 'Wife':
									return '>50K'
								else: return '>50K'
							elif obj[3] == 'Some-college':
								# {"feature": "relationship", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7] == 'Wife':
									return '>50K'
								elif obj[7] == 'Husband':
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Bachelors':
								return '>50K'
							elif obj[3] == 'Assoc-voc':
								return '>50K'
							elif obj[3] == 'Assoc-acdm':
								return '<=50K'
							else: return '<=50K'
						elif float(obj[2])<=30565:
							return '>50K'
						else: return '>50K'
					elif float(obj[0])<=19:
						return '<=50K'
					else: return '<=50K'
				elif float(obj[12])<=38:
					return '<=50K'
				else: return '<=50K'
			else: return '<=50K'
		elif obj[4]>14:
			# {"feature": "age", "instances": 819, "metric_value": 0.9016, "depth": 3}
			if float(obj[0])<=81.80136481799778:
				# {"feature": "capital-loss", "instances": 817, "metric_value": 0.8997, "depth": 4}
				if float(obj[11])<=1766.6154607106769:
					# {"feature": "relationship", "instances": 713, "metric_value": 0.9407, "depth": 5}
					if obj[7] == 'Husband':
						# {"feature": "hours-per-week", "instances": 443, "metric_value": 0.7745, "depth": 6}
						if float(obj[12])>16.88696904929978:
							# {"feature": "fnlwgt", "instances": 424, "metric_value": 0.7413, "depth": 7}
							if float(obj[2])<=453794.0748480455:
								# {"feature": "occupation", "instances": 421, "metric_value": 0.7442, "depth": 8}
								if obj[6] == 'Prof-specialty':
									# {"feature": "native-country", "instances": 344, "metric_value": 0.6869, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "race", "instances": 297, "metric_value": 0.6539, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "workclass", "instances": 283, "metric_value": 0.6568, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "education", "instances": 127, "metric_value": 0.665, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 68, "metric_value": 0.7039, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 68, "metric_value": 0.7039, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[3] == 'Doctorate':
													# {"feature": "marital-status", "instances": 59, "metric_value": 0.6162, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 59, "metric_value": 0.6162, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "education", "instances": 65, "metric_value": 0.7516, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 51, "metric_value": 0.6268, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 51, "metric_value": 0.6268, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[3] == 'Doctorate':
													# {"feature": "marital-status", "instances": 14, "metric_value": 0.9852, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 14, "metric_value": 0.9852, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-inc':
												# {"feature": "education", "instances": 36, "metric_value": 0.4138, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 25, "metric_value": 0.2423, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 25, "metric_value": 0.2423, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[3] == 'Doctorate':
													# {"feature": "marital-status", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'State-gov':
												# {"feature": "education", "instances": 33, "metric_value": 0.6136, "depth": 12}
												if obj[3] == 'Doctorate':
													# {"feature": "marital-status", "instances": 28, "metric_value": 0.5917, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 28, "metric_value": 0.5917, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "education", "instances": 12, "metric_value": 0.65, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[3] == 'Doctorate':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "education", "instances": 10, "metric_value": 0.7219, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[3] == 'Doctorate':
													return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[8] == 'Black':
											# {"feature": "workclass", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[1] == 'Self-emp-inc':
												return '>50K'
											elif obj[1] == 'State-gov':
												# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3] == 'Doctorate':
													return '>50K'
												elif obj[3] == 'Prof-school':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Private':
												return '>50K'
											elif obj[1] == 'Local-gov':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Asian-Pac-Islander':
											# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Self-emp-inc':
												return '>50K'
											elif obj[1] == 'Private':
												return '<=50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Other':
											return '>50K'
										elif obj[8] == 'Amer-Indian-Eskimo':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'India':
										# {"feature": "workclass", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[1] == 'State-gov':
											# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == 'Doctorate':
												# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[3] == 'Prof-school':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Private':
											# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == 'Doctorate':
												# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'Asian-Pac-Islander':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[3] == 'Prof-school':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Federal-gov':
											return '>50K'
										elif obj[1] == 'Self-emp-inc':
											return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Taiwan':
										# {"feature": "workclass", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[1] == 'Private':
											return '>50K'
										elif obj[1] == 'State-gov':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										elif obj[1] == 'Self-emp-not-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Canada':
										# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3] == 'Doctorate':
												# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3] == 'Doctorate':
												# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'China':
										# {"feature": "workclass", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8] == 'Asian-Pac-Islander':
												# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3] == 'Doctorate':
													# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'White':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Federal-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Cuba':
										return '>50K'
									elif obj[13] == 'Philippines':
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Self-emp-inc':
											return '>50K'
										elif obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Local-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Iran':
										return '>50K'
									elif obj[13] == 'England':
										return '>50K'
									elif obj[13] == 'France':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3] == 'Doctorate':
												# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'White':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										else: return '>50K'
									elif obj[13] == 'Columbia':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Federal-gov':
											return '<=50K'
										elif obj[1] == 'State-gov':
											return '>50K'
										else: return '>50K'
									elif obj[13] == 'Germany':
										return '>50K'
									elif obj[13] == 'Haiti':
										return '<=50K'
									elif obj[13] == 'South':
										return '<=50K'
									elif obj[13] == 'Thailand':
										return '>50K'
									elif obj[13] == 'El-Salvador':
										return '>50K'
									elif obj[13] == 'Poland':
										return '>50K'
									elif obj[13] == 'Hong':
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Exec-managerial':
									# {"feature": "race", "instances": 46, "metric_value": 0.7554, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "workclass", "instances": 42, "metric_value": 0.7919, "depth": 10}
										if obj[1] == 'Private':
											# {"feature": "education", "instances": 25, "metric_value": 0.795, "depth": 11}
											if obj[3] == 'Prof-school':
												# {"feature": "marital-status", "instances": 14, "metric_value": 0.9403, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "sex", "instances": 14, "metric_value": 0.9403, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 14, "metric_value": 0.9403, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[3] == 'Doctorate':
												# {"feature": "marital-status", "instances": 11, "metric_value": 0.4395, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "sex", "instances": 11, "metric_value": 0.4395, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 11, "metric_value": 0.4395, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[1] == 'Local-gov':
											# {"feature": "education", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[3] == 'Doctorate':
												# {"feature": "marital-status", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[3] == 'Prof-school':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Self-emp-inc':
											# {"feature": "education", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[3] == 'Doctorate':
												return '>50K'
											elif obj[3] == 'Prof-school':
												# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										elif obj[1] == 'State-gov':
											return '>50K'
										elif obj[1] == 'Self-emp-not-inc':
											# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3] == 'Doctorate':
												# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										else: return '>50K'
									elif obj[8] == 'Asian-Pac-Islander':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Sales':
									# {"feature": "education", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[3] == 'Prof-school':
										# {"feature": "race", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "workclass", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "marital-status", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "marital-status", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-inc':
												return '>50K'
											else: return '>50K'
										elif obj[8] == 'Asian-Pac-Islander':
											return '<=50K'
										else: return '<=50K'
									elif obj[3] == 'Doctorate':
										return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Adm-clerical':
									# {"feature": "workclass", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "education", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[3] == 'Prof-school':
											# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == 'Married-civ-spouse':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'Asian-Pac-Islander':
												return '<=50K'
											else: return '<=50K'
										elif obj[3] == 'Doctorate':
											return '>50K'
										else: return '>50K'
									elif obj[1] == 'State-gov':
										return '>50K'
									elif obj[1] == 'Local-gov':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Craft-repair':
									# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[1] == 'Self-emp-not-inc':
										return '<=50K'
									elif obj[1] == 'Private':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Farming-fishing':
									# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'Self-emp-not-inc':
										# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3] == 'Prof-school':
											# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == 'Married-civ-spouse':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										else: return '>50K'
									else: return '>50K'
								elif obj[6] == 'Tech-support':
									return '<=50K'
								elif obj[6] == 'Protective-serv':
									return '>50K'
								elif obj[6] == 'Machine-op-inspct':
									return '<=50K'
								elif obj[6] == 'Other-service':
									return '<=50K'
								else: return '<=50K'
							elif float(obj[2])>453794.0748480455:
								return '>50K'
							else: return '>50K'
						elif float(obj[12])<=16.88696904929978:
							# {"feature": "occupation", "instances": 19, "metric_value": 0.9495, "depth": 7}
							if obj[6] == 'Prof-specialty':
								# {"feature": "fnlwgt", "instances": 16, "metric_value": 0.9544, "depth": 8}
								if float(obj[2])>88055:
									# {"feature": "race", "instances": 15, "metric_value": 0.971, "depth": 9}
									if obj[8] == 'White':
										# {"feature": "native-country", "instances": 14, "metric_value": 0.9852, "depth": 10}
										if obj[13] == 'United-States':
											# {"feature": "workclass", "instances": 13, "metric_value": 0.9957, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "education", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[3] == 'Doctorate':
													# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "education", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[5] == 'Married-civ-spouse':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												elif obj[3] == 'Doctorate':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											else: return '>50K'
										elif obj[13] == 'Mexico':
											return '<=50K'
										else: return '<=50K'
									elif obj[8] == 'Black':
										return '<=50K'
									else: return '<=50K'
								elif float(obj[2])<=88055:
									return '<=50K'
								else: return '<=50K'
							elif obj[6] == 'Transport-moving':
								return '>50K'
							elif obj[6] == 'Exec-managerial':
								return '<=50K'
							elif obj[6] == 'Farming-fishing':
								return '<=50K'
							else: return '<=50K'
						else: return '<=50K'
					elif obj[7] == 'Not-in-family':
						# {"feature": "hours-per-week", "instances": 182, "metric_value": 0.9894, "depth": 6}
						if float(obj[12])<=82.86462323548994:
							# {"feature": "fnlwgt", "instances": 175, "metric_value": 0.9947, "depth": 7}
							if float(obj[2])<=497784.51958129567:
								# {"feature": "native-country", "instances": 174, "metric_value": 0.9939, "depth": 8}
								if obj[13] == 'United-States':
									# {"feature": "occupation", "instances": 154, "metric_value": 0.9956, "depth": 9}
									if obj[6] == 'Prof-specialty':
										# {"feature": "race", "instances": 125, "metric_value": 0.9866, "depth": 10}
										if obj[8] == 'White':
											# {"feature": "workclass", "instances": 119, "metric_value": 0.9914, "depth": 11}
											if obj[1] == 'Private':
												# {"feature": "marital-status", "instances": 65, "metric_value": 0.971, "depth": 12}
												if obj[5] == 'Never-married':
													# {"feature": "education", "instances": 47, "metric_value": 0.9252, "depth": 13}
													if obj[3] == 'Prof-school':
														# {"feature": "sex", "instances": 26, "metric_value": 0.8905, "depth": 14}
														if obj[9] == 'Female':
															return '<=50K'
														elif obj[9] == 'Male':
															return '<=50K'
														else: return '<=50K'
													elif obj[3] == 'Doctorate':
														# {"feature": "sex", "instances": 21, "metric_value": 0.9587, "depth": 14}
														if obj[9] == 'Male':
															return '<=50K'
														elif obj[9] == 'Female':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												elif obj[5] == 'Divorced':
													# {"feature": "sex", "instances": 12, "metric_value": 0.9799, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "education", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[3] == 'Prof-school':
															return '>50K'
														elif obj[3] == 'Doctorate':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Female':
														# {"feature": "education", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[3] == 'Prof-school':
															return '<=50K'
														elif obj[3] == 'Doctorate':
															return '>50K'
														else: return '>50K'
													else: return '<=50K'
												elif obj[5] == 'Widowed':
													# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9] == 'Female':
														return '<=50K'
													elif obj[9] == 'Male':
														return '>50K'
													else: return '>50K'
												elif obj[5] == 'Separated':
													return '>50K'
												elif obj[5] == 'Married-spouse-absent':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Self-emp-not-inc':
												# {"feature": "sex", "instances": 20, "metric_value": 0.9341, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "marital-status", "instances": 15, "metric_value": 0.8366, "depth": 13}
													if obj[5] == 'Never-married':
														# {"feature": "education", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[3] == 'Doctorate':
															return '>50K'
														elif obj[3] == 'Prof-school':
															return '>50K'
														else: return '>50K'
													elif obj[5] == 'Divorced':
														# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[3] == 'Prof-school':
															return '>50K'
														else: return '>50K'
													elif obj[5] == 'Married-spouse-absent':
														return '>50K'
													elif obj[5] == 'Widowed':
														return '>50K'
													else: return '>50K'
												elif obj[9] == 'Female':
													# {"feature": "education", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[3] == 'Doctorate':
														# {"feature": "marital-status", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[5] == 'Never-married':
															return '<=50K'
														elif obj[5] == 'Divorced':
															return '>50K'
														else: return '>50K'
													elif obj[3] == 'Prof-school':
														# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[5] == 'Never-married':
															return '>50K'
														elif obj[5] == 'Divorced':
															return '<=50K'
														else: return '<=50K'
													else: return '>50K'
												else: return '<=50K'
											elif obj[1] == 'State-gov':
												# {"feature": "marital-status", "instances": 12, "metric_value": 0.9183, "depth": 12}
												if obj[5] == 'Never-married':
													# {"feature": "sex", "instances": 9, "metric_value": 0.7642, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "education", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[3] == 'Doctorate':
															return '<=50K'
														elif obj[3] == 'Prof-school':
															return '>50K'
														else: return '>50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[5] == 'Divorced':
													# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[3] == 'Doctorate':
														return '>50K'
													elif obj[3] == 'Prof-school':
														return '<=50K'
													else: return '<=50K'
												else: return '>50K'
											elif obj[1] == 'Local-gov':
												# {"feature": "marital-status", "instances": 11, "metric_value": 0.684, "depth": 12}
												if obj[5] == 'Divorced':
													return '<=50K'
												elif obj[5] == 'Never-married':
													# {"feature": "sex", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "education", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[3] == 'Prof-school':
															return '<=50K'
														elif obj[3] == 'Doctorate':
															return '<=50K'
														else: return '<=50K'
													elif obj[9] == 'Male':
														return '<=50K'
													else: return '<=50K'
												elif obj[5] == 'Widowed':
													return '<=50K'
												else: return '<=50K'
											elif obj[1] == 'Federal-gov':
												# {"feature": "education", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[5] == 'Never-married':
														# {"feature": "sex", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[9] == 'Female':
															return '>50K'
														elif obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[5] == 'Divorced':
														return '>50K'
													else: return '>50K'
												elif obj[3] == 'Doctorate':
													return '>50K'
												else: return '>50K'
											elif obj[1] == 'Self-emp-inc':
												# {"feature": "education", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[3] == 'Doctorate':
													# {"feature": "marital-status", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[5] == 'Separated':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													elif obj[5] == 'Never-married':
														return '<=50K'
													else: return '<=50K'
												elif obj[3] == 'Prof-school':
													return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[8] == 'Black':
											return '<=50K'
										elif obj[8] == 'Asian-Pac-Islander':
											return '<=50K'
										elif obj[8] == 'Amer-Indian-Eskimo':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Exec-managerial':
										# {"feature": "marital-status", "instances": 17, "metric_value": 0.874, "depth": 10}
										if obj[5] == 'Never-married':
											# {"feature": "workclass", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[1] == 'Private':
												return '>50K'
											elif obj[1] == 'State-gov':
												return '>50K'
											elif obj[1] == 'Local-gov':
												return '>50K'
											elif obj[1] == 'Federal-gov':
												return '<=50K'
											else: return '<=50K'
										elif obj[5] == 'Divorced':
											# {"feature": "race", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "education", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[3] == 'Doctorate':
													# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == 'Private':
														return '>50K'
													elif obj[1] == 'Self-emp-not-inc':
														return '<=50K'
													elif obj[1] == 'Local-gov':
														return '>50K'
													else: return '>50K'
												elif obj[3] == 'Prof-school':
													return '<=50K'
												else: return '<=50K'
											elif obj[8] == 'Black':
												return '>50K'
											else: return '>50K'
										elif obj[5] == 'Widowed':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Sales':
										# {"feature": "workclass", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Self-emp-not-inc':
											# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3] == 'Doctorate':
												return '<=50K'
											elif obj[3] == 'Prof-school':
												return '>50K'
											else: return '>50K'
										elif obj[1] == 'Private':
											return '<=50K'
										else: return '<=50K'
									elif obj[6] == 'Adm-clerical':
										return '<=50K'
									elif obj[6] == 'Craft-repair':
										return '>50K'
									elif obj[6] == 'Other-service':
										# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'Private':
											return '<=50K'
										elif obj[1] == 'Self-emp-inc':
											return '>50K'
										else: return '>50K'
									elif obj[6] == 'Tech-support':
										return '<=50K'
									elif obj[6] == 'Machine-op-inspct':
										return '>50K'
									else: return '>50K'
								elif obj[13] == 'India':
									# {"feature": "workclass", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[6] == 'Prof-specialty':
											# {"feature": "race", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8] == 'Asian-Pac-Islander':
												# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3] == 'Prof-school':
													# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5] == 'Never-married':
														# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == 'Male':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											elif obj[8] == 'Other':
												return '>50K'
											else: return '>50K'
										elif obj[6] == 'Tech-support':
											return '>50K'
										else: return '>50K'
									elif obj[1] == 'State-gov':
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'China':
									return '<=50K'
								elif obj[13] == 'England':
									return '<=50K'
								elif obj[13] == 'Italy':
									# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'State-gov':
										return '>50K'
									elif obj[1] == 'Private':
										return '<=50K'
									else: return '<=50K'
								elif obj[13] == 'Cuba':
									return '<=50K'
								elif obj[13] == 'Canada':
									return '<=50K'
								elif obj[13] == 'Mexico':
									return '>50K'
								elif obj[13] == 'Columbia':
									return '>50K'
								elif obj[13] == 'Taiwan':
									return '>50K'
								elif obj[13] == 'Germany':
									return '<=50K'
								elif obj[13] == 'Japan':
									return '>50K'
								elif obj[13] == 'France':
									return '<=50K'
								else: return '<=50K'
							elif float(obj[2])>497784.51958129567:
								return '>50K'
							else: return '>50K'
						elif float(obj[12])>82.86462323548994:
							return '<=50K'
						else: return '<=50K'
					elif obj[7] == 'Unmarried':
						# {"feature": "workclass", "instances": 35, "metric_value": 0.9518, "depth": 6}
						if obj[1] == 'Private':
							# {"feature": "occupation", "instances": 13, "metric_value": 0.6194, "depth": 7}
							if obj[6] == 'Prof-specialty':
								return '<=50K'
							elif obj[6] == 'Sales':
								return '>50K'
							elif obj[6] == 'Exec-managerial':
								return '>50K'
							elif obj[6] == 'Farming-fishing':
								return '<=50K'
							else: return '<=50K'
						elif obj[1] == 'State-gov':
							# {"feature": "education", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3] == 'Doctorate':
								# {"feature": "fnlwgt", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if float(obj[2])>19520:
									return '>50K'
								elif float(obj[2])<=19520:
									return '<=50K'
								else: return '<=50K'
							elif obj[3] == 'Prof-school':
								return '<=50K'
							else: return '<=50K'
						elif obj[1] == 'Local-gov':
							return '<=50K'
						elif obj[1] == 'Self-emp-not-inc':
							# {"feature": "hours-per-week", "instances": 6, "metric_value": 0.65, "depth": 7}
							if float(obj[12])>10:
								return '>50K'
							elif float(obj[12])<=10:
								return '<=50K'
							else: return '<=50K'
						elif obj[1] == 'Federal-gov':
							return '>50K'
						else: return '>50K'
					elif obj[7] == 'Wife':
						# {"feature": "hours-per-week", "instances": 27, "metric_value": 0.8256, "depth": 6}
						if float(obj[12])>25:
							# {"feature": "occupation", "instances": 24, "metric_value": 0.65, "depth": 7}
							if obj[6] == 'Prof-specialty':
								# {"feature": "fnlwgt", "instances": 20, "metric_value": 0.6098, "depth": 8}
								if float(obj[2])<=247469:
									# {"feature": "workclass", "instances": 18, "metric_value": 0.5033, "depth": 9}
									if obj[1] == 'Private':
										# {"feature": "education", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[3] == 'Prof-school':
											# {"feature": "marital-status", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[5] == 'Married-civ-spouse':
												# {"feature": "race", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "native-country", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[13] == 'United-States':
															return '>50K'
														else: return '>50K'
													else: return '>50K'
												else: return '>50K'
											else: return '>50K'
										elif obj[3] == 'Doctorate':
											# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == 'Married-civ-spouse':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Female':
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[1] == 'State-gov':
										return '>50K'
									elif obj[1] == 'Local-gov':
										return '>50K'
									elif obj[1] == 'Self-emp-inc':
										return '>50K'
									elif obj[1] == 'Federal-gov':
										return '>50K'
									elif obj[1] == 'Self-emp-not-inc':
										return '>50K'
									else: return '>50K'
								elif float(obj[2])>247469:
									# {"feature": "workclass", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'Private':
										return '<=50K'
									elif obj[1] == 'State-gov':
										return '>50K'
									else: return '>50K'
								else: return '<=50K'
							elif obj[6] == 'Exec-managerial':
								return '>50K'
							elif obj[6] == 'Sales':
								return '<=50K'
							else: return '<=50K'
						elif float(obj[12])<=25:
							return '<=50K'
						else: return '<=50K'
					elif obj[7] == 'Own-child':
						# {"feature": "native-country", "instances": 21, "metric_value": 0.5917, "depth": 6}
						if obj[13] == 'United-States':
							# {"feature": "hours-per-week", "instances": 19, "metric_value": 0.4855, "depth": 7}
							if float(obj[12])<=40:
								return '<=50K'
							elif float(obj[12])>40:
								# {"feature": "workclass", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[1] == 'Private':
									# {"feature": "fnlwgt", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if float(obj[2])>80058:
										# {"feature": "marital-status", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[5] == 'Divorced':
											return '<=50K'
										elif obj[5] == 'Never-married':
											return '>50K'
										else: return '>50K'
									elif float(obj[2])<=80058:
										return '<=50K'
									else: return '<=50K'
								elif obj[1] == 'State-gov':
									return '>50K'
								elif obj[1] == 'Self-emp-not-inc':
									return '<=50K'
								else: return '<=50K'
							else: return '<=50K'
						elif obj[13] == 'Italy':
							return '>50K'
						elif obj[13] == 'Philippines':
							return '<=50K'
						else: return '<=50K'
					elif obj[7] == 'Other-relative':
						return '<=50K'
					else: return '<=50K'
				elif float(obj[11])>1766.6154607106769:
					# {"feature": "fnlwgt", "instances": 104, "metric_value": 0.1886, "depth": 5}
					if float(obj[2])>33310:
						# {"feature": "native-country", "instances": 103, "metric_value": 0.1382, "depth": 6}
						if obj[13] == 'United-States':
							# {"feature": "occupation", "instances": 92, "metric_value": 0.0865, "depth": 7}
							if obj[6] == 'Prof-specialty':
								return '>50K'
							elif obj[6] == 'Exec-managerial':
								return '>50K'
							elif obj[6] == 'Sales':
								return '>50K'
							elif obj[6] == 'Tech-support':
								return '>50K'
							elif obj[6] == 'Transport-moving':
								return '<=50K'
							else: return '<=50K'
						elif obj[13] == 'China':
							return '>50K'
						elif obj[13] == 'Germany':
							return '>50K'
						elif obj[13] == 'Honduras':
							return '>50K'
						elif obj[13] == 'Greece':
							return '>50K'
						elif obj[13] == 'Philippines':
							return '>50K'
						elif obj[13] == 'India':
							return '>50K'
						elif obj[13] == 'Taiwan':
							return '>50K'
						elif obj[13] == 'Canada':
							return '<=50K'
						elif obj[13] == 'Hong':
							return '>50K'
						else: return '>50K'
					elif float(obj[2])<=33310:
						return '<=50K'
					else: return '<=50K'
				else: return '>50K'
			elif float(obj[0])>81.80136481799778:
				return '<=50K'
			else: return '<=50K'
		else: return '>50K'
	elif float(obj[10])>8462.827520655317:
		# {"feature": "education-num", "instances": 851, "metric_value": 0.121, "depth": 2}
		if obj[4]>4:
			# {"feature": "age", "instances": 849, "metric_value": 0.1071, "depth": 3}
			if float(obj[0])>17:
				# {"feature": "hours-per-week", "instances": 848, "metric_value": 0.0999, "depth": 4}
				if float(obj[12])>10.441404895537381:
					# {"feature": "workclass", "instances": 835, "metric_value": 0.0859, "depth": 5}
					if obj[1] == 'Private':
						# {"feature": "relationship", "instances": 520, "metric_value": 0.0512, "depth": 6}
						if obj[7] == 'Husband':
							# {"feature": "occupation", "instances": 286, "metric_value": 0.0336, "depth": 7}
							if obj[6] == 'Exec-managerial':
								return '>50K'
							elif obj[6] == 'Prof-specialty':
								return '>50K'
							elif obj[6] == 'Sales':
								return '>50K'
							elif obj[6] == 'Craft-repair':
								# {"feature": "fnlwgt", "instances": 20, "metric_value": 0.2864, "depth": 8}
								if float(obj[2])>108097:
									return '>50K'
								elif float(obj[2])<=108097:
									# {"feature": "education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[3] == 'HS-grad':
										return '>50K'
									elif obj[3] == 'Some-college':
										return '<=50K'
									else: return '<=50K'
								else: return '>50K'
							elif obj[6] == 'Transport-moving':
								return '>50K'
							elif obj[6] == 'Tech-support':
								return '>50K'
							elif obj[6] == 'Adm-clerical':
								return '>50K'
							elif obj[6] == 'Machine-op-inspct':
								return '>50K'
							elif obj[6] == 'Handlers-cleaners':
								return '>50K'
							elif obj[6] == 'Protective-serv':
								return '>50K'
							else: return '>50K'
						elif obj[7] == 'Not-in-family':
							return '>50K'
						elif obj[7] == 'Wife':
							# {"feature": "fnlwgt", "instances": 36, "metric_value": 0.1831, "depth": 7}
							if float(obj[2])<=260540.89098946686:
								return '>50K'
							elif float(obj[2])>260540.89098946686:
								# {"feature": "occupation", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[6] == 'Exec-managerial':
									# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == 'Some-college':
										return '<=50K'
									elif obj[3] == 'Prof-school':
										return '>50K'
									else: return '>50K'
								elif obj[6] == 'Prof-specialty':
									return '>50K'
								elif obj[6] == 'Adm-clerical':
									return '>50K'
								elif obj[6] == 'Sales':
									return '>50K'
								elif obj[6] == 'Craft-repair':
									return '>50K'
								else: return '>50K'
							else: return '>50K'
						elif obj[7] == 'Unmarried':
							return '>50K'
						elif obj[7] == 'Own-child':
							# {"feature": "fnlwgt", "instances": 12, "metric_value": 0.4138, "depth": 7}
							if float(obj[2])<=168981:
								return '>50K'
							elif float(obj[2])>168981:
								# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3] == 'Bachelors':
									return '>50K'
								elif obj[3] == 'HS-grad':
									return '<=50K'
								else: return '<=50K'
							else: return '>50K'
						elif obj[7] == 'Other-relative':
							return '>50K'
						else: return '>50K'
					elif obj[1] == 'Self-emp-inc':
						# {"feature": "fnlwgt", "instances": 122, "metric_value": 0.0686, "depth": 6}
						if float(obj[2])<=290522.1629495724:
							return '>50K'
						elif float(obj[2])>290522.1629495724:
							# {"feature": "education", "instances": 20, "metric_value": 0.2864, "depth": 7}
							if obj[3] == 'Bachelors':
								return '>50K'
							elif obj[3] == 'Masters':
								return '>50K'
							elif obj[3] == 'HS-grad':
								return '>50K'
							elif obj[3] == 'Some-college':
								# {"feature": "occupation", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6] == 'Sales':
									# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == 'Married-civ-spouse':
										# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7] == 'Husband':
											# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8] == 'White':
												# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == 'Male':
													# {"feature": "capital-loss", "instances": 2, "metric_value": 1.0, "depth": 13}
													if float(obj[11])<=0:
														# {"feature": "native-country", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13] == 'United-States':
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									else: return '<=50K'
								elif obj[6] == 'Exec-managerial':
									return '>50K'
								else: return '>50K'
							elif obj[3] == 'Doctorate':
								return '>50K'
							elif obj[3] == 'Prof-school':
								return '>50K'
							else: return '>50K'
						else: return '>50K'
					elif obj[1] == 'Self-emp-not-inc':
						# {"feature": "fnlwgt", "instances": 98, "metric_value": 0.2907, "depth": 6}
						if float(obj[2])>85959.19755976995:
							# {"feature": "occupation", "instances": 83, "metric_value": 0.2243, "depth": 7}
							if obj[6] == 'Prof-specialty':
								# {"feature": "education", "instances": 28, "metric_value": 0.2223, "depth": 8}
								if obj[3] == 'Prof-school':
									return '>50K'
								elif obj[3] == 'Doctorate':
									return '>50K'
								elif obj[3] == 'Bachelors':
									# {"feature": "native-country", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[13] == 'United-States':
										# {"feature": "marital-status", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'Married-civ-spouse':
											# {"feature": "relationship", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == 'Husband':
												# {"feature": "race", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == 'White':
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == 'Male':
														# {"feature": "capital-loss", "instances": 2, "metric_value": 1.0, "depth": 14}
														if float(obj[11])<=0:
															return '<=50K'
														else: return '<=50K'
													else: return '<=50K'
												else: return '<=50K'
											else: return '<=50K'
										else: return '<=50K'
									elif obj[13] == 'Japan':
										return '>50K'
									else: return '>50K'
								elif obj[3] == 'Assoc-voc':
									return '>50K'
								elif obj[3] == 'HS-grad':
									return '>50K'
								elif obj[3] == 'Masters':
									return '>50K'
								else: return '>50K'
							elif obj[6] == 'Sales':
								return '>50K'
							elif obj[6] == 'Exec-managerial':
								# {"feature": "marital-status", "instances": 16, "metric_value": 0.3373, "depth": 8}
								if obj[5] == 'Married-civ-spouse':
									return '>50K'
								elif obj[5] == 'Divorced':
									# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[9] == 'Female':
										return '>50K'
									elif obj[9] == 'Male':
										# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3] == 'Masters':
											return '>50K'
										elif obj[3] == 'HS-grad':
											return '<=50K'
										else: return '<=50K'
									else: return '>50K'
								elif obj[5] == 'Never-married':
									return '>50K'
								else: return '>50K'
							elif obj[6] == 'Craft-repair':
								return '>50K'
							elif obj[6] == 'Farming-fishing':
								# {"feature": "education", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[3] == 'HS-grad':
									return '>50K'
								elif obj[3] == 'Some-college':
									return '>50K'
								elif obj[3] == 'Masters':
									return '<=50K'
								else: return '<=50K'
							elif obj[6] == 'Adm-clerical':
								return '>50K'
							elif obj[6] == 'Machine-op-inspct':
								return '>50K'
							else: return '>50K'
						elif float(obj[2])<=85959.19755976995:
							# {"feature": "relationship", "instances": 15, "metric_value": 0.5665, "depth": 7}
							if obj[7] == 'Husband':
								# {"feature": "occupation", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[6] == 'Prof-specialty':
									return '>50K'
								elif obj[6] == 'Sales':
									return '>50K'
								elif obj[6] == 'Craft-repair':
									return '<=50K'
								elif obj[6] == 'Exec-managerial':
									return '>50K'
								else: return '>50K'
							elif obj[7] == 'Not-in-family':
								return '>50K'
							elif obj[7] == 'Wife':
								return '<=50K'
							elif obj[7] == 'Other-relative':
								return '>50K'
							else: return '>50K'
						else: return '>50K'
					elif obj[1] == 'Local-gov':
						return '>50K'
					elif obj[1] == 'State-gov':
						return '>50K'
					elif obj[1] == 'Federal-gov':
						return '>50K'
					else: return '>50K'
				elif float(obj[12])<=10.441404895537381:
					# {"feature": "marital-status", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[5] == 'Married-civ-spouse':
						return '>50K'
					elif obj[5] == 'Never-married':
						return '<=50K'
					elif obj[5] == 'Widowed':
						return '>50K'
					else: return '>50K'
				else: return '>50K'
			elif float(obj[0])<=17:
				return '<=50K'
			else: return '<=50K'
		elif obj[4]<=4:
			return '<=50K'
		else: return '<=50K'
	else: return '>50K'
