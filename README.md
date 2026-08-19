# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 520
- HTTP: 401 alive / 159 gold
- HTTPS: 262 alive / 83 gold
- SOCKS4: 222 alive / 142 gold
- SOCKS5: 215 alive / 136 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18509
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
