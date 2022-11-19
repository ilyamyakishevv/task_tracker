"""deleted added

Revision ID: 368c605c45de
Revises: 3d7101d2321e
Create Date: 2022-11-04 15:07:17.889750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '368c605c45de'
down_revision = '3d7101d2321e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('changes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_changes_description'), 'changes', ['description'], unique=False)
    op.create_index(op.f('ix_changes_name'), 'changes', ['name'], unique=True)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('role')
    )
    op.create_table('actions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('action_user', sa.Integer(), nullable=True),
    sa.Column('action_object', sa.Integer(), nullable=True),
    sa.Column('action_description', sa.Integer(), nullable=True),
    sa.Column('action_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['action_description'], ['changes.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['action_object'], ['tasks.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['action_user'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_actions_action_description'), 'actions', ['action_description'], unique=False)
    op.create_index(op.f('ix_actions_action_object'), 'actions', ['action_object'], unique=False)
    op.create_index(op.f('ix_actions_action_user'), 'actions', ['action_user'], unique=False)
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_task_id'), 'comment', ['task_id'], unique=False)
    op.create_index(op.f('ix_comment_user_id'), 'comment', ['user_id'], unique=False)
    op.add_column('tasks', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    op.drop_column('users', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone', sa.INTEGER(), nullable=True))
    op.drop_column('tasks', 'is_deleted')
    op.drop_index(op.f('ix_comment_user_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_task_id'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_actions_action_user'), table_name='actions')
    op.drop_index(op.f('ix_actions_action_object'), table_name='actions')
    op.drop_index(op.f('ix_actions_action_description'), table_name='actions')
    op.drop_table('actions')
    op.drop_table('roles')
    op.drop_index(op.f('ix_changes_name'), table_name='changes')
    op.drop_index(op.f('ix_changes_description'), table_name='changes')
    op.drop_table('changes')
    # ### end Alembic commands ###