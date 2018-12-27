; Ben Bitdiddle has invented a test to determine
; whether the interpreter he is faced with is using
; applicative-order evaluation or normal-order
;evaluation.  He defines the following two procedures:

(define (p) (p))
(define (test x y)
    (if (= x 0) 0 y))

; Then he evaluates the expression

(test 0 (p))

;What behavior will Ben observe with an interpreter that uses
;applicative-order evaluation? What behavior will he observe with
;an interpreter that uses normal-rder evaluation? Explain your answer.
;(Assume that the evaluation rules the special form if is the same
;whether the interpreter is using normal or applicative order: The
;predicate expression is evaluted first, and the result determines
;whether to evaluate the consequent or the altenrative expression.)

;--------------
;On an applicate-order evaluation interpreter such as the one we use
;in scheme the function will run indefinitely since it will 
;expand p recursively


; were it normal order evaluation it would return 0 because
; once it fully exapnded the test for the first operator it 
; immediately evaluate to 0, bypassin the evaluation of (p)
