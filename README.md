# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 395
- HTTP: 380 alive / 88 gold
- HTTPS: 283 alive / 14 gold
- SOCKS4: 226 alive / 129 gold
- SOCKS5: 255 alive / 164 gold

## Historical pool

- Discovered: 131855
- Ever alive: 21326
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
