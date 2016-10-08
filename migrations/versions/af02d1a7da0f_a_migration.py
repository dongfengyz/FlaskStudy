"""a migration

Revision ID: af02d1a7da0f
Revises: None
Create Date: 2016-09-06 16:10:10.293000

"""

# revision identifiers, used by Alembic.
revision = 'af02d1a7da0f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=sa.TEXT(length=64),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=sa.TEXT(length=64),
               nullable=False)
    ### end Alembic commands ###