# SyndProxy validated proxy pool

## Current pool

- Alive now: 331
- Gold now: 292
- HTTP: 34 alive / 26 gold
- HTTPS: 2 alive / 0 gold
- SOCKS4: 148 alive / 143 gold
- SOCKS5: 147 alive / 123 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43628
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
