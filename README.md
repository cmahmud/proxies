# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 407
- HTTP: 98 alive / 63 gold
- HTTPS: 79 alive / 19 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38640
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
