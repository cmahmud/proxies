# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 407
- HTTP: 109 alive / 66 gold
- HTTPS: 82 alive / 12 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38122
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
