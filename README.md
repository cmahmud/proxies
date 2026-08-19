# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 280
- HTTP: 303 alive / 65 gold
- HTTPS: 237 alive / 18 gold
- SOCKS4: 191 alive / 99 gold
- SOCKS5: 193 alive / 98 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15414
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
