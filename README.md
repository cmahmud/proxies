# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 405
- HTTP: 285 alive / 83 gold
- HTTPS: 169 alive / 22 gold
- SOCKS4: 206 alive / 154 gold
- SOCKS5: 251 alive / 146 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32376
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
