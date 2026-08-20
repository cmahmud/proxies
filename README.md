# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 409
- HTTP: 215 alive / 85 gold
- HTTPS: 166 alive / 23 gold
- SOCKS4: 212 alive / 147 gold
- SOCKS5: 265 alive / 154 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27442
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
