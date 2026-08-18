# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 354
- HTTP: 405 alive / 53 gold
- HTTPS: 208 alive / 13 gold
- SOCKS4: 224 alive / 141 gold
- SOCKS5: 237 alive / 147 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14869
- Ever gold: 477

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
