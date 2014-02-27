(define (domain store)
   (:constants agent) 
   (:predicates (at ?package ?comptoir)
                (to ?package ?comptoir)
                (pos ?agent ?position)
                (loadedOn ?package)
                (loadedOff ?package)
        (delivered ?package)
        (node ?comptoir)
        (package ?package)
        (connected ?origin ?destination)
        )
  (:functions (poids ?package)
          (maxLoad ?agent)
          (loadWeight ?agent)
          (costNode ?origin ?destination)
          (cost ?agent))
  (:action take
       :parameters  (?package ?comptoir)
       :precondition (and (at ?package ?comptoir)
                          (>= (maxLoad agent) (+ (loadWeight agent) (poids ?package)))
                          (not (to ?package ?comptoir))
                          (package ?package)
                          (node ?comptoir)

       )
       :effect (and (not (at ?package ?comptoir))
                    (increase (loadWeight agent) (poids ?package))
        
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
                    (decrease (loadWeight agent) (poids ?package))
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
                     (increase (cost agent) (costNode ?origin ?destination))
                )
       )
  )