# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 394
- HTTP: 89 alive / 67 gold
- HTTPS: 86 alive / 16 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 168 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43337
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
