# SyndProxy private pool

## Current pool

- Alive now: 1384
- Gold now: 416
- HTTP: 521 alive / 85 gold
- HTTPS: 329 alive / 16 gold
- SOCKS4: 263 alive / 157 gold
- SOCKS5: 271 alive / 158 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20807
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
