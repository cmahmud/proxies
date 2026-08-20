# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 417
- HTTP: 300 alive / 95 gold
- HTTPS: 237 alive / 28 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 233 alive / 158 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27601
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
