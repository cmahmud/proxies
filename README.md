# SyndProxy validated proxy pool

## Current pool

- Alive now: 345
- Gold now: 304
- HTTP: 39 alive / 28 gold
- HTTPS: 3 alive / 0 gold
- SOCKS4: 152 alive / 142 gold
- SOCKS5: 151 alive / 134 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43623
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
