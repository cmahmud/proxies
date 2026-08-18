# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 244
- HTTP: 469 alive / 24 gold
- HTTPS: 261 alive / 10 gold
- SOCKS4: 205 alive / 109 gold
- SOCKS5: 226 alive / 101 gold

## Historical pool

- Discovered: 94370
- Ever alive: 10159
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
