# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 407
- HTTP: 89 alive / 58 gold
- HTTPS: 87 alive / 21 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42718
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
