"""empty message

Revision ID: f43ee5e5efd5
Revises: f2a468e80441
Create Date: 2024-06-04 19:09:15.632950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f43ee5e5efd5'
down_revision = 'f2a468e80441'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likerecipes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipi_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipi_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likerecipes')
    # ### end Alembic commands ###
