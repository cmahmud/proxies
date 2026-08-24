# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 388
- HTTP: 124 alive / 56 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 194 alive / 162 gold

## Historical pool

- Discovered: 178292
- Ever alive: 33367
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
