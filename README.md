# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 260
- HTTP: 216 alive / 33 gold
- HTTPS: 126 alive / 8 gold
- SOCKS4: 231 alive / 126 gold
- SOCKS5: 227 alive / 93 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9105
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
