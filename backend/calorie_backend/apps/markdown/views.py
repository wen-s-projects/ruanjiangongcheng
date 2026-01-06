from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import markdown
from bleach import clean


@api_view(['POST'])
@permission_classes([AllowAny])
def preview(request):
    markdown_text = request.data.get('markdown', '')

    try:
        html = markdown.markdown(
            markdown_text,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.sane_lists',
            ]
        )

        cleaned_html = clean(
            html,
            tags={
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                'p', 'br', 'hr',
                'strong', 'em', 'u', 'del',
                'ul', 'ol', 'li',
                'blockquote', 'code', 'pre',
                'a', 'img',
                'table', 'thead', 'tbody', 'tr', 'th', 'td',
            },
            attributes={
                'a': ['href', 'title', 'target'],
                'img': ['src', 'alt', 'title', 'width', 'height'],
                '*': ['class', 'id'],
            },
            styles=[],
            strip=True
        )

        return Response({'html': cleaned_html})
    except Exception as e:
        return Response(
            {'error': f'渲染失败: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
