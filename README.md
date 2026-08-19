# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 526
- HTTP: 354 alive / 160 gold
- HTTPS: 245 alive / 89 gold
- SOCKS4: 210 alive / 133 gold
- SOCKS5: 227 alive / 144 gold

## Historical pool

- Discovered: 123075
- Ever alive: 18700
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
