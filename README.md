# SyndProxy private pool

## Current pool

- Alive now: 1335
- Gold now: 386
- HTTP: 450 alive / 93 gold
- HTTPS: 327 alive / 16 gold
- SOCKS4: 268 alive / 137 gold
- SOCKS5: 290 alive / 140 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21594
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
