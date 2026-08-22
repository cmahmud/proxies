# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 423
- HTTP: 268 alive / 96 gold
- HTTPS: 137 alive / 27 gold
- SOCKS4: 201 alive / 145 gold
- SOCKS5: 245 alive / 155 gold

## Historical pool

- Discovered: 167122
- Ever alive: 32542
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
