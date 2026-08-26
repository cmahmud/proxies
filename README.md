# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 385
- HTTP: 139 alive / 67 gold
- HTTPS: 180 alive / 20 gold
- SOCKS4: 166 alive / 146 gold
- SOCKS5: 182 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39720
- Ever gold: 1301

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
