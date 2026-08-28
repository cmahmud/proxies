# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 393
- HTTP: 102 alive / 69 gold
- HTTPS: 78 alive / 11 gold
- SOCKS4: 159 alive / 157 gold
- SOCKS5: 172 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43105
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
