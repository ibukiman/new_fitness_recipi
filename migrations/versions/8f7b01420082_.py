"""empty message

Revision ID: 8f7b01420082
Revises: e885ede1d4f1
Create Date: 2024-06-04 20:37:02.524457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f7b01420082'
down_revision = 'e885ede1d4f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aiueo_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('aiueo', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aiueo_table')
    # ### end Alembic commands ###