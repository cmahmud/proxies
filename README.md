# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 377
- HTTP: 194 alive / 82 gold
- HTTPS: 127 alive / 21 gold
- SOCKS4: 211 alive / 132 gold
- SOCKS5: 215 alive / 142 gold

## Historical pool

- Discovered: 155683
- Ever alive: 29200
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
