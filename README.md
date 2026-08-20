# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 386
- HTTP: 201 alive / 74 gold
- HTTPS: 164 alive / 27 gold
- SOCKS4: 214 alive / 128 gold
- SOCKS5: 215 alive / 157 gold

## Historical pool

- Discovered: 150519
- Ever alive: 27053
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
