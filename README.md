# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 403
- HTTP: 93 alive / 61 gold
- HTTPS: 76 alive / 18 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38582
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
