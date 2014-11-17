"""empty message

Revision ID: 14ec7d678ee
Revises: 89d0c07291
Create Date: 2014-11-17 00:22:41.900426

"""

# revision identifiers, used by Alembic.
revision = '14ec7d678ee'
down_revision = '89d0c07291'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('editor', sa.String(length=255), nullable=True))
    op.add_column('books', sa.Column('publisher', sa.String(length=255), nullable=True))
    op.add_column('books', sa.Column('subtitle', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'subtitle')
    op.drop_column('books', 'publisher')
    op.drop_column('books', 'editor')
    ### end Alembic commands ###
