# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 391
- HTTP: 88 alive / 67 gold
- HTTPS: 73 alive / 13 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 170 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43414
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
