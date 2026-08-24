# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 438
- HTTP: 138 alive / 80 gold
- HTTPS: 105 alive / 24 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 197 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34553
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
