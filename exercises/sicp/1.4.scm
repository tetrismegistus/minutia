; Observe that our model of evaluation allows
; for combinations whose operators are compound expressions
; Use this observation to describe the behavior of the
; following procedure

(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))

;the operator for the procedure is the result of the if statement
;the operator evaluates to a single operator 
;plus or minus depending on whether b is positive or neg

