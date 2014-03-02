
(define (problem prob1)
   (:domain store)
   (:objects A B C D E F G H I p818)
   (:init 
   (= (cost agent) 0)
      (package p818)
      (= (poids p818) 2)
      (at p818 A)
      (to p818 G)

      (node A)
      (node B)
      (node C)
      (node D)
      (node E)
      (node F)
      (node G)
      (node H)
      (node I)

      (= (maxLoad agent) 5)
      (= (loadWeight agent) 0)
      (pos agent E)

      (connected A C)
      (connected C A)
      (= (costNode C A) 2)
      (= (costNode A C) 2)

      (connected B C)
      (connected C B)
      (= (costNode C B) 3)
      (= (costNode B C) 3)

      (connected C D)
      (connected D C)
      (= (costNode D C) 3)
      (= (costNode C D) 3)

      (connected D E)
      (connected E D)
      (= (costNode E D) 4)
      (= (costNode D E) 4)

      (connected D F)
      (connected F D)
      (= (costNode F D) 4)
      (= (costNode D F) 4)

      (connected C H)
      (connected H C)
      (= (costNode H C) 5)
      (= (costNode C H) 5)

      (connected G H)
      (connected H G)
      (= (costNode H G) 3)
      (= (costNode G H) 3)

      (connected H I)
      (connected I H)
      (= (costNode I H) 4)
      (= (costNode H I) 4)

   )

   (:goal (forall (?x) (imply (package ?x) (delivered ?x))))
   (:metric minimize (cost agent)))
