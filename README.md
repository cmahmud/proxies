# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 422
- HTTP: 99 alive / 74 gold
- HTTPS: 77 alive / 26 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 169 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41773
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
