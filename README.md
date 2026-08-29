# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 401
- HTTP: 89 alive / 68 gold
- HTTPS: 75 alive / 15 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43280
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
