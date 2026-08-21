# SyndProxy private pool

## Current pool

- Alive now: 1337
- Gold now: 421
- HTTP: 534 alive / 99 gold
- HTTPS: 346 alive / 25 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 240 alive / 157 gold

## Historical pool

- Discovered: 159278
- Ever alive: 30401
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
