# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 376
- HTTP: 331 alive / 81 gold
- HTTPS: 239 alive / 27 gold
- SOCKS4: 158 alive / 105 gold
- SOCKS5: 258 alive / 163 gold

## Historical pool

- Discovered: 166669
- Ever alive: 32474
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
