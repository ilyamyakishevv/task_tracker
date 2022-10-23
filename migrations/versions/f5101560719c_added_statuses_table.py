"""added statuses table

Revision ID: f5101560719c
Revises: 6e9e512cdceb
Create Date: 2022-10-21 16:03:19.970462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5101560719c'
down_revision = '6e9e512cdceb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_statuses_description'), 'statuses', ['description'], unique=False)
    op.create_index(op.f('ix_statuses_name'), 'statuses', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_statuses_name'), table_name='statuses')
    op.drop_index(op.f('ix_statuses_description'), table_name='statuses')
    op.drop_table('statuses')
    # ### end Alembic commands ###
