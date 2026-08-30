# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 442
- HTTP: 109 alive / 82 gold
- HTTPS: 53 alive / 27 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43687
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
