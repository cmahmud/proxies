# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 398
- HTTP: 78 alive / 61 gold
- HTTPS: 48 alive / 14 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42831
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
