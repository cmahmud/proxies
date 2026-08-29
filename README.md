# SyndProxy validated proxy pool

## Current pool

- Alive now: 435
- Gold now: 378
- HTTP: 56 alive / 47 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 169 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43528
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
