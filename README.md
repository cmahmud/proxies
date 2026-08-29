# SyndProxy validated proxy pool

## Current pool

- Alive now: 348
- Gold now: 272
- HTTP: 36 alive / 26 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 154 alive / 129 gold
- SOCKS5: 157 alive / 117 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43619
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
