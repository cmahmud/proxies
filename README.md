# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 405
- HTTP: 238 alive / 86 gold
- HTTPS: 193 alive / 24 gold
- SOCKS4: 219 alive / 133 gold
- SOCKS5: 260 alive / 162 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32127
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
