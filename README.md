# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 407
- HTTP: 103 alive / 65 gold
- HTTPS: 59 alive / 19 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38960
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
