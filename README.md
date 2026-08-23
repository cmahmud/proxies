# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 370
- HTTP: 89 alive / 50 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 161 alive / 153 gold
- SOCKS5: 180 alive / 155 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33041
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
