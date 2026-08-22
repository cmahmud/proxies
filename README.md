# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 421
- HTTP: 321 alive / 94 gold
- HTTPS: 277 alive / 30 gold
- SOCKS4: 193 alive / 130 gold
- SOCKS5: 260 alive / 167 gold

## Historical pool

- Discovered: 161925
- Ever alive: 31179
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
