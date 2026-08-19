# SyndProxy private pool

## Current pool

- Alive now: 1380
- Gold now: 392
- HTTP: 479 alive / 90 gold
- HTTPS: 314 alive / 20 gold
- SOCKS4: 259 alive / 128 gold
- SOCKS5: 328 alive / 154 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22034
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
