# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 406
- HTTP: 96 alive / 63 gold
- HTTPS: 62 alive / 17 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39075
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
