# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 428
- HTTP: 131 alive / 80 gold
- HTTPS: 101 alive / 21 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34065
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
