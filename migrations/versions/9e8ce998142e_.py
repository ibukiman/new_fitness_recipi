"""empty message

Revision ID: 9e8ce998142e
Revises: f43ee5e5efd5
Create Date: 2024-06-04 19:13:04.590904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e8ce998142e'
down_revision = 'f43ee5e5efd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('likerecipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('like_now', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('likerecipes', schema=None) as batch_op:
        batch_op.drop_column('like_now')

    # ### end Alembic commands ###
