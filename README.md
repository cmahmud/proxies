# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 297
- HTTP: 389 alive / 65 gold
- HTTPS: 223 alive / 16 gold
- SOCKS4: 204 alive / 117 gold
- SOCKS5: 190 alive / 99 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15597
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
