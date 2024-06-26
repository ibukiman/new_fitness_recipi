"""empty message

Revision ID: 31e5a5db1c0d
Revises: 03c2efc2a42e
Create Date: 2024-06-05 14:11:35.064048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31e5a5db1c0d'
down_revision = '03c2efc2a42e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likerecipes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likerecipes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('recipi_id', sa.INTEGER(), nullable=False),
    sa.Column('like_now', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
