# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 394
- HTTP: 308 alive / 89 gold
- HTTPS: 247 alive / 32 gold
- SOCKS4: 219 alive / 144 gold
- SOCKS5: 240 alive / 129 gold

## Historical pool

- Discovered: 160993
- Ever alive: 30908
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
