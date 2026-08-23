# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 369
- HTTP: 82 alive / 48 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 183 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33041
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
