
(define (problem prob1)
   (:domain store)
   (:objects A B C D E F G H I p2102 p5431)
   (:init 
      (package p2102)
      (= (poids p2102) 2)
      (at p2102 B)
      (to p2102 A)

      (package p5431)
      (= (poids p5431) 4)
      (at p5431 B)
      (to p5431 A)

      (node A)
      (node B)
      (node C)
      (node D)
      (node E)
      (node F)
      (node G)
      (node H)
      (node I)

      (= maxLoad 5)
      (= loadWeight 0)
      (pos agent A)

      (connected A C)
      (connected C A)
      (= (cost C A) 2)
      (= (cost A C) 2)

      (connected B C)
      (connected C B)
      (= (cost C B) 3)
      (= (cost B C) 3)

      (connected C D)
      (connected D C)
      (= (cost D C) 3)
      (= (cost C D) 3)

      (connected D E)
      (connected E D)
      (= (cost E D) 4)
      (= (cost D E) 4)

      (connected D F)
      (connected F D)
      (= (cost F D) 4)
      (= (cost D F) 4)

      (connected C H)
      (connected H C)
      (= (cost H C) 5)
      (= (cost C H) 5)

      (connected G H)
      (connected H G)
      (= (cost H G) 3)
      (= (cost G H) 3)

      (connected H I)
      (connected I H)
      (= (cost I H) 4)
      (= (cost H I) 4)

   )

   (:goal (forall (?x) (imply (package ?x) (delivered ?x))))
   (:metric minimize (cost agent)))
