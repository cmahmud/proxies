# SyndProxy private pool

## Current pool

- Alive now: 632
- Gold now: 383
- HTTP: 165 alive / 68 gold
- HTTPS: 98 alive / 16 gold
- SOCKS4: 178 alive / 145 gold
- SOCKS5: 191 alive / 154 gold

## Historical pool

- Discovered: 146602
- Ever alive: 25684
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
