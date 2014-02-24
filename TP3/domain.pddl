(define (domain store)
   (:constants maxLoad loadWeight) 
   (:predicates (at ?package ?comptoir)
                (to ?package ?comptoir)
                (pos ?agent ?position)
                (loadedOn ?package)
                (loadedOff ?package)
                (package ?package)
                (delivered ?package)
                (node ?comptoir))
  (:action take
       :parameters  (?package ?comptoir)
       :precondition (and (at ?package ?comptoir)
                          (>= (maxLoad) (+ (loadWeight) (poids ?package)))
                          (not (to ?package ?comptoir))
                          (package ?package)
                          (node ?comptoir)

       )
       :effect (and (not (at ?package ?comptoir))
                    (increase (loadWeight) (poids ?package))
        
       )
  )
  (:action drop
       :parameters  (?package ?comptoir)
       :precondition (and (not (at ?package ?comptoir))
                          (to ?package ?comptoir)
                          (package ?package)
                          (node ?comptoir)
       )
       :effect (and (at ?package ?comptoir)
                    (decrease (loadWeight) (poids ?package))
                    (delivered ?package)
       )
  )
  (:action move
       :parameters  (?origin ?destination)
       :precondition (and (not (pos agent ?destination))
                          (connected ?origin ?destination)
                          (node ?origin)
                          (node ?destination)
       )
       :effect  (and (pos agent ?destination)
                     (increase (cost) (cost ?origin ?destination))
                )
       )
  )