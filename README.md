# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 379
- HTTP: 102 alive / 65 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 166 alive / 150 gold
- SOCKS5: 176 alive / 150 gold

## Historical pool

- Discovered: 176956
- Ever alive: 33251
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
