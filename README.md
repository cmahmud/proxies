# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 382
- HTTP: 85 alive / 57 gold
- HTTPS: 76 alive / 11 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 172 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43426
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
