; Exercise 1.6: Alyssa P. Hacker doesn't see why if needs to
; be provided as a special form.  "Why can't I just define it as
; an ordinary procedure in terms of cond?" she asks. Alyssa's
; friend Eva Lu Ator claims this can indeed be done, and she
; defines a new version of if:

(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)
        )
  )

; Eva demonstrates the program for Ayssa:
(new-if (= 2 3) 0 5)
; 5
(new-if (= 1 1) 0 5)
; 0

;Delighted, Alyssa uses new-if to rewrite the square-root
;program:

(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
          guess
          (sqrt-iter (improve guess x) x)
          )
  )

; What happens when Alyssa attempt to use this to computer
; square roots? Explain.
; ------------------------
; Infinite recursion.  Because.
; The (cond) special form returns the actual expression
; specified for the matching true preicate, it does not return the 
; evaluated expression.
;
; The (if) special form returns the evaluated expression.  
;
; (good-enough?)  depends on knowing if the second clause is true
; or false but can never determine the truth of the second clause
; because it is now receiving a recursive expression instead of
; an evaluted truth conditon
;--------------------------
;The above answer did not prove to be correct
; new-if being a procedure all the arguments are evaluated on the function 
; call -  one of the arguments is a recursive call..
