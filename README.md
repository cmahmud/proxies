# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 432
- HTTP: 305 alive / 87 gold
- HTTPS: 225 alive / 28 gold
- SOCKS4: 242 alive / 156 gold
- SOCKS5: 270 alive / 161 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32203
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
