# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 304
- HTTP: 381 alive / 65 gold
- HTTPS: 223 alive / 17 gold
- SOCKS4: 210 alive / 117 gold
- SOCKS5: 200 alive / 105 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15595
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
