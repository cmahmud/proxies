# SyndProxy validated proxy pool

## Current pool

- Alive now: 432
- Gold now: 361
- HTTP: 59 alive / 38 gold
- HTTPS: 34 alive / 6 gold
- SOCKS4: 162 alive / 154 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43585
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
