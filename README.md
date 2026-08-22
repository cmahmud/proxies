# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 401
- HTTP: 254 alive / 101 gold
- HTTPS: 179 alive / 28 gold
- SOCKS4: 201 alive / 141 gold
- SOCKS5: 234 alive / 131 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31785
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
