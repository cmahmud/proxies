# SyndProxy private pool

## Current pool

- Alive now: 735
- Gold now: 353
- HTTP: 224 alive / 65 gold
- HTTPS: 136 alive / 17 gold
- SOCKS4: 183 alive / 132 gold
- SOCKS5: 192 alive / 139 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25771
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
