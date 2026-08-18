# SyndProxy private pool

## Current pool

- Alive now: 885
- Gold now: 246
- HTTP: 289 alive / 29 gold
- HTTPS: 135 alive / 7 gold
- SOCKS4: 231 alive / 117 gold
- SOCKS5: 230 alive / 93 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9081
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
