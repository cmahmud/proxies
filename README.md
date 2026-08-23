# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 371
- HTTP: 74 alive / 51 gold
- HTTPS: 39 alive / 13 gold
- SOCKS4: 177 alive / 154 gold
- SOCKS5: 180 alive / 153 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33045
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
