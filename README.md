# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 405
- HTTP: 88 alive / 55 gold
- HTTPS: 106 alive / 19 gold
- SOCKS4: 180 alive / 167 gold
- SOCKS5: 193 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41514
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
