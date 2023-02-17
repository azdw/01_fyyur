"""empty message

Revision ID: 0b14fe123512
Revises: caffeeec1dcb
Create Date: 2023-02-13 17:46:42.180742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b14fe123512'
down_revision = 'caffeeec1dcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seeking_venue', sa.Boolean(), nullable=True))
        batch_op.drop_column('looking_for_venues')

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seeking_talent', sa.Boolean(), nullable=True))
        batch_op.drop_column('looking_for_talent')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('looking_for_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.drop_column('seeking_talent')

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('looking_for_venues', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.drop_column('seeking_venue')

    # ### end Alembic commands ###