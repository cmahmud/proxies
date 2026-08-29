# SyndProxy validated proxy pool

## Current pool

- Alive now: 377
- Gold now: 339
- HTTP: 45 alive / 33 gold
- HTTPS: 3 alive / 1 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 166 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43597
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
