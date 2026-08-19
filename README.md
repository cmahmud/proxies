# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 500
- HTTP: 396 alive / 136 gold
- HTTPS: 255 alive / 89 gold
- SOCKS4: 194 alive / 122 gold
- SOCKS5: 238 alive / 153 gold

## Historical pool

- Discovered: 119650
- Ever alive: 17834
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
