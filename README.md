# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 363
- HTTP: 86 alive / 63 gold
- HTTPS: 72 alive / 17 gold
- SOCKS4: 164 alive / 147 gold
- SOCKS5: 168 alive / 136 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43457
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
