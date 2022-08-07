"""create User table

Revision ID: 985874ad9896
Revises: 42b1235c222b
Create Date: 2022-08-07 11:53:16.587354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '985874ad9896'
down_revision = '42b1235c222b'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('users')
