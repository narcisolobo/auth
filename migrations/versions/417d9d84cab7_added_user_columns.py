"""added user columns

Revision ID: 417d9d84cab7
Revises: 
Create Date: 2023-07-29 23:33:23.076728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '417d9d84cab7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avatar', sa.String(length=60), nullable=True))
        batch_op.add_column(sa.Column('location', sa.String(length=60), nullable=True))
        batch_op.add_column(sa.Column('blurb', sa.String(length=280), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('blurb')
        batch_op.drop_column('location')
        batch_op.drop_column('avatar')

    # ### end Alembic commands ###
