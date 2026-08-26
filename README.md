# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 401
- HTTP: 105 alive / 58 gold
- HTTPS: 80 alive / 13 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38255
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
