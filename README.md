# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 387
- HTTP: 79 alive / 49 gold
- HTTPS: 57 alive / 13 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41626
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
