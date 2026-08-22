# SyndProxy private pool

## Current pool

- Alive now: 850
- Gold now: 421
- HTTP: 258 alive / 95 gold
- HTTPS: 152 alive / 26 gold
- SOCKS4: 204 alive / 145 gold
- SOCKS5: 236 alive / 155 gold

## Historical pool

- Discovered: 167122
- Ever alive: 32542
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
