# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 374
- HTTP: 99 alive / 51 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 189 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33034
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
