# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 408
- HTTP: 111 alive / 66 gold
- HTTPS: 91 alive / 13 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38128
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
