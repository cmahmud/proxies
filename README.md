# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 407
- HTTP: 103 alive / 64 gold
- HTTPS: 88 alive / 17 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38364
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
