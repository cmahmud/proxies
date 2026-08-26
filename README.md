# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 412
- HTTP: 108 alive / 68 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38960
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
