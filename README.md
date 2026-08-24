# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 431
- HTTP: 125 alive / 77 gold
- HTTPS: 87 alive / 25 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34661
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
