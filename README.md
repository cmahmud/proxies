# SyndProxy validated proxy pool

## Current pool

- Alive now: 410
- Gold now: 325
- HTTP: 53 alive / 31 gold
- HTTPS: 23 alive / 2 gold
- SOCKS4: 160 alive / 140 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43564
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
