# SyndProxy validated proxy pool

## Current pool

- Alive now: 351
- Gold now: 308
- HTTP: 46 alive / 26 gold
- HTTPS: 13 alive / 0 gold
- SOCKS4: 146 alive / 143 gold
- SOCKS5: 146 alive / 139 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43631
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
