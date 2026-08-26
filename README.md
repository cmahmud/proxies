# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 398
- HTTP: 96 alive / 58 gold
- HTTPS: 95 alive / 13 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 195 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39266
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
