# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 405
- HTTP: 94 alive / 63 gold
- HTTPS: 49 alive / 16 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42836
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
