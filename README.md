# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 403
- HTTP: 98 alive / 59 gold
- HTTPS: 60 alive / 18 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38993
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
