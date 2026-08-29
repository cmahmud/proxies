# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 352
- HTTP: 74 alive / 47 gold
- HTTPS: 61 alive / 11 gold
- SOCKS4: 168 alive / 146 gold
- SOCKS5: 176 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43509
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
