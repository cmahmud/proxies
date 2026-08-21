# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 412
- HTTP: 367 alive / 99 gold
- HTTPS: 195 alive / 21 gold
- SOCKS4: 215 alive / 137 gold
- SOCKS5: 286 alive / 155 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27926
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
