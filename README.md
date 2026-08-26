# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 375
- HTTP: 122 alive / 67 gold
- HTTPS: 64 alive / 19 gold
- SOCKS4: 149 alive / 139 gold
- SOCKS5: 169 alive / 150 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38770
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
