# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 401
- HTTP: 69 alive / 54 gold
- HTTPS: 56 alive / 24 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42783
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
