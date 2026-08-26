# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 405
- HTTP: 98 alive / 60 gold
- HTTPS: 77 alive / 16 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39173
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
