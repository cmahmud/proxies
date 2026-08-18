# SyndProxy private pool

## Current pool

- Alive now: 1192
- Gold now: 248
- HTTP: 484 alive / 27 gold
- HTTPS: 266 alive / 10 gold
- SOCKS4: 211 alive / 109 gold
- SOCKS5: 231 alive / 102 gold

## Historical pool

- Discovered: 94370
- Ever alive: 10169
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
