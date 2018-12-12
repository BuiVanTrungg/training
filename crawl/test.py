def visitBinaryOp(self, ast, o): 
        #ast: BinaryOp
        #o: Any
		
        ctxt = o
        frame = ctxt.frame		
        nenv = ctxt.sym
        lval = 0
        rval = 1
				
        if ast.op == '=': 
            if type(ast.left) is Id:
                 if type(ast.right) is Id:
                       right_type = self.visit(ast.right,(Access(frame,nenv,False,True),lval))
                 elif type(ast.right) is ArrayCell:
                       right_type = self.visit(ast.right,(Access(frame,nenv,False,True),lval))
                       if type(ast.right.idx) is not ArrayCell:
                            self.emit.printout(self.emit.emitPUSHICONST(ast.right.idx.value,frame))									   
					   
                       right_type = self.visit(ast.right,(Access(frame,nenv,False,False),lval))					   
                 else:				 
                       right_type = self.visit(ast.right,Access(frame,nenv,False,True))
					   
#                 if type(ast.right) is BinaryOp:
#                       if ast.right.op == '=':
#                            self.emit.printout(self.emit.emitDUP(frame))									   
				 
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,True),rval))
            elif type(ast.left) is ArrayCell:
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval))
                 self.emit.printout(self.emit.emitPUSHICONST(ast.left.idx.value,frame))
			
                 if type(ast.right) is Id:
                       right_type = self.visit(ast.right,(Access(frame,nenv,False,True),lval))
                 elif type(ast.right) is ArrayCell:
                       right_type = self.visit(ast.right,(Access(frame,nenv,False,True),lval))
                       if type(ast.right.idx) is not ArrayCell:
                            self.emit.printout(self.emit.emitPUSHICONST(ast.right.idx.value,frame))									   					   
                       right_type = self.visit(ast.right,(Access(frame,nenv,False,False),lval))					   					   
                 else:
                       right_type = self.visit(ast.right,Access(frame,nenv,False,True))
                 ass_type = self.visit(ast.left,(Access(frame,nenv,False,False),rval))
        elif ast.op == '||':
            if type(ast.left) is Id:
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 	
            elif type(ast.left) is ArrayCell:
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 
                 self.emit.printout(self.emit.emitPUSHICONST(ast.left.idx.value,frame)) 				 
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,False),lval)) 				 				 
            else:
                 left_type = self.visit(ast.left,Access(frame,nenv,True,True)) 	
					   
            end_label = frame.getNewLabel()
            self.emit.printout(self.emit.emitDUP(frame))
            self.emit.printout(self.emit.emitIFNE(end_label,frame))
						
            if type(ast.right) is Id:
                 right_type = self.visit(ast.right,(Access(frame,nenv,False,True),lval)) 		
            elif type(ast.right) is ArrayCell:
                 right_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 
                 self.emit.printout(self.emit.emitPUSHICONST(ast.right.idx.value,frame)) 				 
                 right_type = self.visit(ast.left,(Access(frame,nenv,False,False),lval)) 				 				 
            else:
                 right_type = self.visit(ast.right,Access(frame,nenv,True,True)) 					
					   
            self.emit.printout(self.emit.emitOROP(frame))
            self.emit.printout(self.emit.emitLABEL(end_label,frame))
            return BoolType()

        elif ast.op == '&&':
            if type(ast.left) is Id:
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 	
            elif type(ast.left) is ArrayCell:
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 
                 self.emit.printout(self.emit.emitPUSHICONST(ast.left.idx.value,frame)) 				 
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,False),lval)) 				 				 
            else:
                 left_type = self.visit(ast.left,Access(frame,nenv,True,True)) 	

					   
            end_label = frame.getNewLabel()
            self.emit.printout(self.emit.emitDUP(frame))
            self.emit.printout(self.emit.emitIFEQ(end_label,frame))
						
            if type(ast.right) is Id:
                 right_type = self.visit(ast.right,(Access(frame,nenv,False,True),lval)) 		
            elif type(ast.right) is ArrayCell:
                 right_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 
                 self.emit.printout(self.emit.emitPUSHICONST(ast.right.idx.value,frame)) 				 
                 right_type = self.visit(ast.left,(Access(frame,nenv,False,False),lval)) 				 				 
            else:
                 right_type = self.visit(ast.right,Access(frame,nenv,True,True)) 					
					   
            self.emit.printout(self.emit.emitANDOP(frame))
            self.emit.printout(self.emit.emitLABEL(end_label,frame))
            return BoolType()
				 
        else:
            if type(ast.left) is Id:
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 	
            elif type(ast.left) is ArrayCell:
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 
                 self.emit.printout(self.emit.emitPUSHICONST(ast.left.idx.value,frame)) 				 
                 left_type = self.visit(ast.left,(Access(frame,nenv,False,False),lval)) 				 
            else:
                 left_type = self.visit(ast.left,Access(frame,nenv,True,False)) 	

#            if type(left_type) is IntType:
#                 self.emit.printout(self.emit.emitI2F(frame)) 	
					   
            if type(ast.right) is Id:
                 right_type = self.visit(ast.right,(Access(frame,nenv,False,True),lval)) 							 
            elif type(ast.right) is ArrayCell:
                 right_type = self.visit(ast.left,(Access(frame,nenv,False,True),lval)) 
                 self.emit.printout(self.emit.emitPUSHICONST(ast.right.idx.value,frame)) 				 
                 right_type = self.visit(ast.left,(Access(frame,nenv,False,False),lval)) 				 
            else:
                 right_type = self.visit(ast.right,Access(frame,nenv,True,False)) 					
					   
#            if type(right_type) is IntType:
#                 self.emit.printout(self.emit.emitI2F(frame)) 	
					   
			
            if ast.op == '+' or ast.op == '-': 			
                 if type(left_type) is FloatType or type(right_type) is FloatType:		
                       self.emit.printout(self.emit.emitADDOP(ast.op,FloatType(),frame))
                       return FloatType()
                 elif type(left_type) is IntType and type(right_type) is IntType:
                       self.emit.printout(self.emit.emitADDOP(ast.op,IntType(),frame))
                       return IntType()
                 else:				 
                       raise IllegalOperandException("Kieu khong hop le")					   
            elif ast.op == '*' or ast.op == '/': 			
                 if type(left_type) is FloatType or type(right_type) is FloatType:		
                       self.emit.printout(self.emit.emitMULOP(ast.op,FloatType(),frame))
                       return FloatType()
                 elif type(left_type) is IntType and type(right_type) is IntType:
                       self.emit.printout(self.emit.emitMULOP(ast.op,IntType(),frame))
                       return IntType()
                 else:
                       raise IllegalOperandException("Kieu khong hop le")
            elif ast.op == '%': 		
                 if type(left_type) is IntType and type(right_type) is IntType:			
                       self.emit.printout(self.emit.emitMOD(frame))
                       return IntType()
                 else:				 				 
                       raise IllegalOperandException("Kieu khong hop le")
            elif ast.op == '<' or ast.op == '<=' or ast.op == '>' or ast.op == '>=' or ast.op == '!=' or ast.op == '==': 	
                 if type(left_type) is FloatType or type(right_type) is FloatType:	
                       self.emit.printout(self.emit.emitREOP(ast.op,FloatType(),frame))
                       return BoolType()
                 elif type(left_type) is IntType and type(right_type) is IntType:	
                       self.emit.printout(self.emit.emitREOP(ast.op,IntType(),frame))
                       return BoolType()
                 else:				 				 
                       raise IllegalOperandException("Kieu khong hop le")