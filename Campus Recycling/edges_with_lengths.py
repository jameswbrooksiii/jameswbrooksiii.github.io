edges_with_lengths(dictionary):
     # East and Northeast Part of Main Campus
    {"Early Childhood Education Center": [("College of Business", 3.5), ("IESB", 3), ("Tech Pointe", 4)],
     "IESB": [("College of Business", 2), ("Early Childhood Education Center", 3), ("Tech Pointe", 1), ("Nethken Hall", 4)], 
     "College of Business": [("Tech Pointe", 3), ("IESB", 2), ("Prescott Library/Wyly Tower", 4), ("University Hall", 1.5), ("Early Childhood Education Center", 3.5)],
     "University Hall": [("Keeny Hall", 1)],
     "Keeny Hall": [("Bogard Hall", 1)],
     "Bogard Hall": [("Howard Auditorium", 2.5), ("Tech Pointe", 2), ("College of Business", 1.5), ("Davison Hall", 7), ("Biomedical Engineering Building", 9)],
     "Tech Pointe": [("Nethken Hall", 3.5) ("College of Business", 3), ("IESB", 1), ("Early Childhood Education Center", 4), ("Howard Auditorium", 2.5), ("Davison Hall", 7), ("Biomedical Engineering Building", 9)],
     "Nethken Hall": [("Tech Pointe", 3.5), ("IESB", 4), ("Engineering Annex", 0.5), ("Carson-Taylor Hall", 1), ("Howard Auditorium", 4.5), ("Davison Hall", 6), ("Biomedical Engineering Building", 8)],
     "Engineering Annex": [("Nethken Hall", 0.5), ("Carson-Taylor Hall", 0.75)],
     "Carson-Taylor Hall": [("Engineering Annex", 0.75), ("Nethken Hall", 1)],
     "Howard Auditorium": [("KLPI Radio Station", 0.5), ("Tech Pointe", 2.5), ("Davison Hall", 5), ("Biomedical Engineering Building", 7), ("Nethken Hall", 4.5)],
     "KLPI Radio Station": [("Howard Auditorium", 0.5)],
     # Railroad Ave (North Part of Main Campus) + Richardson Hall
     "Prescott Library/Wyly Tower": [("College of Business", 4), ("University Hall", 3.5), ("GTM Hall", 2)],
     "GTM Hall": [("Ropp Center", 3.5), ("Hale Hall", 3), ("Richardson Hall", 7)],
     "Richardson Hall": [("GTM Hall", 7.5), ("University Police", 4), ("Institute for Micromanufacturing", 7), ("Hale Hall", 6.5)],
     # Mayfield Street
     "Hale Hall": [("Robinson Hall", 0.5), ("Memorial Gymnasium", 1), ("GTM Hall", 3), ("Richardson Hall", 6.5), ("Ropp Center", 4)],
     "Robinson Hall": [("Hale Hall", 0.5), ("Memorial Gymnasium", 1.1)],
     "Memorial Gymnasium": [("Hale Hall", 1), ("Robinson Hall", 1.1), ("F. Jay Taylor Center", 3)],
     "F. Jay Taylor Center": [("Memorial Gymnasium", 3), ("University Police", 0.5)],
     "University Police": [("F. Jay Taylor Center", 0.5), ("Richardson Hall", 4), ("Institute of Micromanufacturing", 6), ("Power Plant", 2.5)],
     # Nelson Ave
     "Institute of Micromanufacturing": [("Richardson Hall", 7), ("University Police", 6), ("Biomedical Engineering Building", 0.5)],
     "Biomedical Engineering Building": [("Institute of Micromanufacturing", 0.5), ("Tech Pointe", 9), ("Nethken Hall", 8), ("Howard Auditorium", 7), ("Davison Hall", 5)],
     # Hergot Ave
     "Davison Hall": [("Tech Pointe", 7), ("Nethken Hall", 6), ("Howard Auditorium", 5), ("Adams Hall", 1), ("Biomedical Engineering Building", 5)],
     "Adams Hall": [("Davison Hall", 1), ("T.H. Harris", 0.5)],
     "T.H. Harris": [("Adams Hall", 0.5), ("Power Plant", 1.5), ("Landscape Shop", 2.5)],
     "Power Plant": [("T.H. Harris", 1.5), ("University Hall", 2.5), ("Landscape Shop", 3)],
     # Wisteria Dr
     "Landscape Shop": [("Power Plant", 3), ("T.H. Harris", 2.5), ("Tolliver Hall", 1)],
     "Tolliver Hall": [("Landscape Shop", 1), ("Woodward Hall", 2), ("Ropp Center", 2.5), ("Student Center", 3)],
     "Woodward Hall": [("Tolliver Hall", 2), ("Band Building", 0.5)],
     "Band Building": [("Woodward Hall", 0.5), ("Planetarium", 1)],
     "Planetarium": [("Band Building", 1)],
     "Ropp Center": [("GTM Hall", 3.5), ("Tolliver Hall", 2.5), ("Hale Hall", 4), ("Student Center", 1.5)],
     "Student Center": [("Ropp Center", 1.5), ("Barnes and Noble", 0.5)],
     "Barnes and Noble": [("Student Center", 0.5)]
     }
     
