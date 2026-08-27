# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 408
- HTTP: 90 alive / 60 gold
- HTTPS: 73 alive / 17 gold
- SOCKS4: 184 alive / 165 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41560
- Ever gold: 1338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
