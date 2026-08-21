# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 381
- HTTP: 245 alive / 69 gold
- HTTPS: 180 alive / 17 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 232 alive / 152 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29571
- Ever gold: 1130

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
