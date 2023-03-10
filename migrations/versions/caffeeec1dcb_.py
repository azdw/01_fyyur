"""empty message

Revision ID: caffeeec1dcb
Revises: db07832f3b63
Create Date: 2023-02-12 21:49:06.604799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caffeeec1dcb'
down_revision = 'db07832f3b63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.alter_column('looking_for_venues',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True)

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('looking_for_talent',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('looking_for_talent',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.alter_column('looking_for_venues',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
