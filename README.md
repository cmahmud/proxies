# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 401
- HTTP: 99 alive / 62 gold
- HTTPS: 107 alive / 16 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41430
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
