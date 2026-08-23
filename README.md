# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 376
- HTTP: 89 alive / 60 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 185 alive / 155 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33101
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
