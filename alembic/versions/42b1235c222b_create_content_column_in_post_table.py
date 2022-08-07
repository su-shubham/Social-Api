"""create_content_column_in_post_table

Revision ID: 42b1235c222b
Revises: ae57aeaf9378
Create Date: 2022-08-07 11:43:34.182111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42b1235c222b'
down_revision = 'ae57aeaf9378'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')