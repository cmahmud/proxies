# SyndProxy private pool

## Current pool

- Alive now: 1222
- Gold now: 463
- HTTP: 469 alive / 124 gold
- HTTPS: 301 alive / 73 gold
- SOCKS4: 227 alive / 138 gold
- SOCKS5: 225 alive / 128 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16717
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
