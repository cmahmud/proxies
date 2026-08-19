# SyndProxy private pool

## Current pool

- Alive now: 1001
- Gold now: 300
- HTTP: 386 alive / 65 gold
- HTTPS: 222 alive / 16 gold
- SOCKS4: 201 alive / 117 gold
- SOCKS5: 192 alive / 102 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15595
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
