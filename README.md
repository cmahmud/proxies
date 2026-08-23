# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 378
- HTTP: 81 alive / 53 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33036
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
