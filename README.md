# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 396
- HTTP: 92 alive / 64 gold
- HTTPS: 99 alive / 10 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43051
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
