# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 404
- HTTP: 108 alive / 61 gold
- HTTPS: 94 alive / 12 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 199 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38153
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
