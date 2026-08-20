# SyndProxy private pool

## Current pool

- Alive now: 707
- Gold now: 370
- HTTP: 162 alive / 68 gold
- HTTPS: 147 alive / 23 gold
- SOCKS4: 197 alive / 134 gold
- SOCKS5: 201 alive / 145 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26648
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
