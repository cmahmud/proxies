# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 368
- HTTP: 216 alive / 72 gold
- HTTPS: 105 alive / 14 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 196 alive / 132 gold

## Historical pool

- Discovered: 145558
- Ever alive: 25469
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
