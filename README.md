# SyndProxy private pool

## Current pool

- Alive now: 671
- Gold now: 250
- HTTP: 157 alive / 36 gold
- HTTPS: 98 alive / 8 gold
- SOCKS4: 218 alive / 125 gold
- SOCKS5: 198 alive / 81 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9350
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
