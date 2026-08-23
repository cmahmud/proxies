# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 373
- HTTP: 74 alive / 51 gold
- HTTPS: 38 alive / 14 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 179 alive / 154 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33045
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
