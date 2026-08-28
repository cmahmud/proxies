# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 402
- HTTP: 98 alive / 64 gold
- HTTPS: 107 alive / 17 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43011
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
