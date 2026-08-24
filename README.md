# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 423
- HTTP: 129 alive / 73 gold
- HTTPS: 112 alive / 21 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33857
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
