# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 203
- HTTP: 283 alive / 22 gold
- HTTPS: 126 alive / 10 gold
- SOCKS4: 221 alive / 100 gold
- SOCKS5: 219 alive / 71 gold

## Historical pool

- Discovered: 91529
- Ever alive: 8342
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
