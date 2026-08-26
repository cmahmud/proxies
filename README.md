# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 406
- HTTP: 94 alive / 63 gold
- HTTPS: 79 alive / 15 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39180
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
