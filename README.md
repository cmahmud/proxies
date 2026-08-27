# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 422
- HTTP: 102 alive / 74 gold
- HTTPS: 129 alive / 23 gold
- SOCKS4: 180 alive / 158 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42103
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
