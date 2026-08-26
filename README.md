# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 405
- HTTP: 109 alive / 62 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38966
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
