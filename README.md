# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 413
- HTTP: 94 alive / 67 gold
- HTTPS: 103 alive / 15 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42576
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
