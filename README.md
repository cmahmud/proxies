# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 443
- HTTP: 401 alive / 100 gold
- HTTPS: 270 alive / 30 gold
- SOCKS4: 244 alive / 154 gold
- SOCKS5: 276 alive / 159 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30446
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
