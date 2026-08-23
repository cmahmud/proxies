# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 374
- HTTP: 110 alive / 50 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 185 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33034
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
