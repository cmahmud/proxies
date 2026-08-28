# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 401
- HTTP: 85 alive / 60 gold
- HTTPS: 49 alive / 14 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42837
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
