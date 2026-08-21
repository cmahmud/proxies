# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 407
- HTTP: 289 alive / 97 gold
- HTTPS: 205 alive / 23 gold
- SOCKS4: 201 alive / 135 gold
- SOCKS5: 256 alive / 152 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27898
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
