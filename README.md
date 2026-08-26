# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 403
- HTTP: 94 alive / 60 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39044
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
