# SyndProxy private pool

## Current pool

- Alive now: 948
- Gold now: 378
- HTTP: 296 alive / 80 gold
- HTTPS: 215 alive / 24 gold
- SOCKS4: 211 alive / 134 gold
- SOCKS5: 226 alive / 140 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29369
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
