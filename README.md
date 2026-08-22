# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 407
- HTTP: 253 alive / 95 gold
- HTTPS: 189 alive / 32 gold
- SOCKS4: 215 alive / 139 gold
- SOCKS5: 222 alive / 141 gold

## Historical pool

- Discovered: 163253
- Ever alive: 31753
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
