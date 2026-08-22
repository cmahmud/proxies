# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 397
- HTTP: 230 alive / 86 gold
- HTTPS: 187 alive / 24 gold
- SOCKS4: 216 alive / 132 gold
- SOCKS5: 242 alive / 155 gold

## Historical pool

- Discovered: 162771
- Ever alive: 31659
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
