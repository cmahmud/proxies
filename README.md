# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 397
- HTTP: 348 alive / 88 gold
- HTTPS: 179 alive / 19 gold
- SOCKS4: 211 alive / 129 gold
- SOCKS5: 257 alive / 161 gold

## Historical pool

- Discovered: 157414
- Ever alive: 29710
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
