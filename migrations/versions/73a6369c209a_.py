"""empty message

Revision ID: 73a6369c209a
Revises: f9b9f34b6027
Create Date: 2024-06-04 20:27:22.858255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73a6369c209a'
down_revision = 'f9b9f34b6027'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likerecipes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipi_id', sa.Integer(), nullable=False),
    sa.Column('like_now', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipi_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likerecipes')
    # ### end Alembic commands ###
