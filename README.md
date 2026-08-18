# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 305
- HTTP: 405 alive / 31 gold
- HTTPS: 237 alive / 4 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 208 alive / 128 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13423
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
