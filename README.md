# SyndProxy private pool

## Current pool

- Alive now: 1182
- Gold now: 382
- HTTP: 389 alive / 92 gold
- HTTPS: 278 alive / 21 gold
- SOCKS4: 219 alive / 125 gold
- SOCKS5: 296 alive / 144 gold

## Historical pool

- Discovered: 134557
- Ever alive: 22140
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
