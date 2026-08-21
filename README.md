# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 430
- HTTP: 320 alive / 111 gold
- HTTPS: 193 alive / 36 gold
- SOCKS4: 219 alive / 138 gold
- SOCKS5: 236 alive / 145 gold

## Historical pool

- Discovered: 160263
- Ever alive: 30734
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
