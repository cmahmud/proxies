# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 377
- HTTP: 115 alive / 67 gold
- HTTPS: 60 alive / 20 gold
- SOCKS4: 149 alive / 139 gold
- SOCKS5: 171 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38772
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
