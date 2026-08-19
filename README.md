# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 526
- HTTP: 353 alive / 160 gold
- HTTPS: 236 alive / 89 gold
- SOCKS4: 208 alive / 133 gold
- SOCKS5: 227 alive / 144 gold

## Historical pool

- Discovered: 122729
- Ever alive: 18700
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
