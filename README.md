# SyndProxy validated proxy pool

## Current pool

- Alive now: 452
- Gold now: 371
- HTTP: 75 alive / 54 gold
- HTTPS: 39 alive / 11 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 170 alive / 153 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33047
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
