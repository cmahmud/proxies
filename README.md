# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 405
- HTTP: 95 alive / 61 gold
- HTTPS: 74 alive / 15 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39176
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
