# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 326
- HTTP: 52 alive / 40 gold
- HTTPS: 33 alive / 4 gold
- SOCKS4: 163 alive / 142 gold
- SOCKS5: 170 alive / 140 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43545
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
