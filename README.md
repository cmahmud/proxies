# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 405
- HTTP: 74 alive / 57 gold
- HTTPS: 57 alive / 19 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41577
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
