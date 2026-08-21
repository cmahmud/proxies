# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 411
- HTTP: 322 alive / 98 gold
- HTTPS: 294 alive / 31 gold
- SOCKS4: 234 alive / 156 gold
- SOCKS5: 226 alive / 126 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30271
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
