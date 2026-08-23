# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 376
- HTTP: 79 alive / 56 gold
- HTTPS: 56 alive / 10 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 179 alive / 155 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
