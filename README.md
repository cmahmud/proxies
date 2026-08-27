# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 411
- HTTP: 93 alive / 61 gold
- HTTPS: 89 alive / 18 gold
- SOCKS4: 180 alive / 165 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41563
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
