# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 389
- HTTP: 88 alive / 65 gold
- HTTPS: 83 alive / 13 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 166 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43378
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
