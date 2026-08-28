# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 369
- HTTP: 97 alive / 66 gold
- HTTPS: 81 alive / 12 gold
- SOCKS4: 162 alive / 143 gold
- SOCKS5: 173 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43176
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
