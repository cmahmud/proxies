# SyndProxy private pool

## Current pool

- Alive now: 690
- Gold now: 372
- HTTP: 170 alive / 82 gold
- HTTPS: 101 alive / 21 gold
- SOCKS4: 201 alive / 136 gold
- SOCKS5: 218 alive / 133 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25948
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
