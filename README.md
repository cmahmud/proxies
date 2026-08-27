# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 393
- HTTP: 81 alive / 54 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41580
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
