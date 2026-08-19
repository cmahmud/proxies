# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 496
- HTTP: 318 alive / 149 gold
- HTTPS: 237 alive / 90 gold
- SOCKS4: 194 alive / 122 gold
- SOCKS5: 214 alive / 135 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17589
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
