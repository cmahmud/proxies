# SyndProxy private pool

## Current pool

- Alive now: 649
- Gold now: 251
- HTTP: 161 alive / 35 gold
- HTTPS: 87 alive / 7 gold
- SOCKS4: 206 alive / 125 gold
- SOCKS5: 195 alive / 84 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9351
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
