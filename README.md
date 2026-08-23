# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 365
- HTTP: 88 alive / 46 gold
- HTTPS: 35 alive / 11 gold
- SOCKS4: 177 alive / 153 gold
- SOCKS5: 193 alive / 155 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33027
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
