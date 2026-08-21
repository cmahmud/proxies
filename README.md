# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 436
- HTTP: 327 alive / 96 gold
- HTTPS: 227 alive / 29 gold
- SOCKS4: 216 alive / 145 gold
- SOCKS5: 259 alive / 166 gold

## Historical pool

- Discovered: 158917
- Ever alive: 30132
- Ever gold: 1141

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
