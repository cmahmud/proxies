# SyndProxy validated proxy pool

## Current pool

- Alive now: 454
- Gold now: 377
- HTTP: 70 alive / 51 gold
- HTTPS: 45 alive / 7 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43519
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
