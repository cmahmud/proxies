# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 304
- HTTP: 302 alive / 63 gold
- HTTPS: 231 alive / 18 gold
- SOCKS4: 189 alive / 118 gold
- SOCKS5: 193 alive / 105 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15445
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
