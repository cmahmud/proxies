# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 394
- HTTP: 107 alive / 69 gold
- HTTPS: 85 alive / 11 gold
- SOCKS4: 159 alive / 156 gold
- SOCKS5: 172 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43101
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
