# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 401
- HTTP: 71 alive / 53 gold
- HTTPS: 49 alive / 19 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47105
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
