# SyndProxy validated proxy pool

## Current pool

- Alive now: 438
- Gold now: 347
- HTTP: 85 alive / 45 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 157 alive / 147 gold
- SOCKS5: 154 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43640
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
