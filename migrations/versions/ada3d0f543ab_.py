"""empty message

Revision ID: ada3d0f543ab
Revises: 018acf950548
Create Date: 2022-04-10 14:16:50.605446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ada3d0f543ab'
down_revision = '018acf950548'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lessons', sa.Column('student', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lessons', 'student')
    # ### end Alembic commands ###
