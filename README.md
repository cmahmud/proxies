# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 411
- HTTP: 180 alive / 78 gold
- HTTPS: 142 alive / 24 gold
- SOCKS4: 201 alive / 140 gold
- SOCKS5: 247 alive / 169 gold

## Historical pool

- Discovered: 155791
- Ever alive: 29333
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
