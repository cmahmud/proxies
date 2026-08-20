# SyndProxy private pool

## Current pool

- Alive now: 681
- Gold now: 384
- HTTP: 157 alive / 75 gold
- HTTPS: 123 alive / 21 gold
- SOCKS4: 208 alive / 148 gold
- SOCKS5: 193 alive / 140 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26238
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
