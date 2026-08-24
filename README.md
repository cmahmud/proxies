# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 431
- HTTP: 129 alive / 78 gold
- HTTPS: 93 alive / 24 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34620
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
