# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 387
- HTTP: 89 alive / 65 gold
- HTTPS: 81 alive / 8 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43210
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
