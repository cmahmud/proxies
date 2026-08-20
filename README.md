# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 408
- HTTP: 182 alive / 81 gold
- HTTPS: 162 alive / 24 gold
- SOCKS4: 208 alive / 156 gold
- SOCKS5: 227 alive / 147 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26969
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
