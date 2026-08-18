# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 330
- HTTP: 276 alive / 51 gold
- HTTPS: 201 alive / 12 gold
- SOCKS4: 226 alive / 135 gold
- SOCKS5: 218 alive / 132 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14954
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
