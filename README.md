# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 398
- HTTP: 307 alive / 87 gold
- HTTPS: 184 alive / 24 gold
- SOCKS4: 208 alive / 128 gold
- SOCKS5: 247 alive / 159 gold

## Historical pool

- Discovered: 166560
- Ever alive: 32404
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
