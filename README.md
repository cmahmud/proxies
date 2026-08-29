# SyndProxy validated proxy pool

## Current pool

- Alive now: 331
- Gold now: 261
- HTTP: 32 alive / 14 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 148 alive / 141 gold
- SOCKS5: 150 alive / 106 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43625
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
