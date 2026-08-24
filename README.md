# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 430
- HTTP: 124 alive / 81 gold
- HTTPS: 72 alive / 20 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33949
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
