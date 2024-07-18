from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from tasks.models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'equipment_name', 'equipment_category', 'equipment_sub_category', 'equipment_model', 'equipment_type', 'equipment_scale', 'equipment_cost', 'equipment_description', 'equipment_availability', 'equipment_skill','equipment_damage', 'equipment_use_notes','source')
        
class EquipmentView(ViewSet):
    """Equipment table API for CRUD"""
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        if isinstance(data, list):
            created_equipment = []
            for piece in data:
                serializer = EquipmentSerializer(data=piece)
                if serializer.is_valid():
                    piece = serializer.save()
                    created_equipment.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(created_equipment, status=status.HTTP_201_CREATED)
        else:
            serializer = EquipmentSerializer(data=data)
            if serializer.is_valid():
                piece = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        """Get a single piece of equipment by pk"""
        try:
            piece = Equipment.objects.get(pk=pk)
            serializer = EquipmentSerializer(piece)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Equipment.DoesNotExist:
            raise NotFound(detail="Piece of equipment not found", code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        """List all equipment"""
        pieces = Equipment.objects.all()
        serializer = EquipmentSerializer(pieces, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        """Update a piece of equipment"""
        try:
            piece = Equipment.objects.get(pk=pk)
            serializer = EquipmentSerializer(piece, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Equipment.DoesNotExist:
            return Response({"error": "Piece of equipment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        """Delete a piece of equipment"""
        try:
            piece = Equipment.objects.get(pk=pk)
            piece.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Equipment.DoesNotExist:
            return Response({"error": "Piece of equipment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)