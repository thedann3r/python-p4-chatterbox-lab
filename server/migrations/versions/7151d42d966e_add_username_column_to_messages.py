"""Add username column to messages

Revision ID: 7151d42d966e
Revises: 5df667133bc9
Create Date: 2025-01-19 12:59:55.366144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7151d42d966e'
down_revision = '5df667133bc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('username', sa.String(), nullable=False))
    op.drop_column('messages', 'user_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('user_name', sa.VARCHAR(), nullable=False))
    op.drop_column('messages', 'username')
    # ### end Alembic commands ###
