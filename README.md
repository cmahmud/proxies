# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 376
- HTTP: 260 alive / 84 gold
- HTTPS: 151 alive / 21 gold
- SOCKS4: 184 alive / 119 gold
- SOCKS5: 227 alive / 152 gold

## Historical pool

- Discovered: 166324
- Ever alive: 32394
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
