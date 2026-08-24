# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 433
- HTTP: 142 alive / 79 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 191 alive / 161 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33951
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
