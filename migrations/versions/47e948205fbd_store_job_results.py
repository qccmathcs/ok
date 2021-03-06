"""Store job results

Revision ID: 47e948205fbd
Revises: 50937c69da0b
Create Date: 2016-12-26 22:25:26.072381

"""

# revision identifiers, used by Alembic.
revision = '47e948205fbd'
down_revision = '50937c69da0b'

from alembic import op
import sqlalchemy as sa
import server
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('result', mysql.MEDIUMTEXT(), nullable=True))
    op.add_column('job', sa.Column('result_kind', sa.Enum('html', 'string', 'link', name='result_kind'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'result_kind')
    op.drop_column('job', 'result')
    # ### end Alembic commands ###
