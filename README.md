# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 397
- HTTP: 84 alive / 55 gold
- HTTPS: 58 alive / 16 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42839
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
