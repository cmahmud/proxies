# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 422
- HTTP: 107 alive / 75 gold
- HTTPS: 120 alive / 21 gold
- SOCKS4: 180 alive / 158 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42109
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
