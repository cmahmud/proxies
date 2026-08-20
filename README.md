# SyndProxy private pool

## Current pool

- Alive now: 1939
- Gold now: 701
- HTTP: 761 alive / 234 gold
- HTTPS: 604 alive / 146 gold
- SOCKS4: 240 alive / 155 gold
- SOCKS5: 334 alive / 166 gold

## Historical pool

- Discovered: 142709
- Ever alive: 24432
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
