# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 382
- HTTP: 281 alive / 87 gold
- HTTPS: 168 alive / 19 gold
- SOCKS4: 205 alive / 111 gold
- SOCKS5: 250 alive / 165 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32435
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
