# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 384
- HTTP: 90 alive / 63 gold
- HTTPS: 74 alive / 10 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 168 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43446
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
