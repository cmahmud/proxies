# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 411
- HTTP: 108 alive / 63 gold
- HTTPS: 95 alive / 19 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38426
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
