# SyndProxy private pool

## Current pool

- Alive now: 764
- Gold now: 365
- HTTP: 192 alive / 87 gold
- HTTPS: 150 alive / 20 gold
- SOCKS4: 218 alive / 132 gold
- SOCKS5: 204 alive / 126 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26610
- Ever gold: 1084

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
