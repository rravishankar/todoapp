"""empty message

Revision ID: ffd4cec04bde
Revises: 640bc390ca27
Create Date: 2020-05-15 10:34:08.478315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffd4cec04bde'
down_revision = '640bc390ca27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    #Added later by Ravi
    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
    op.alter_column('todos', 'completed', nullable=False)

    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
