# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 378
- HTTP: 238 alive / 78 gold
- HTTPS: 119 alive / 15 gold
- SOCKS4: 225 alive / 150 gold
- SOCKS5: 196 alive / 135 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25462
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
