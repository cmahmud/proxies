# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 441
- HTTP: 134 alive / 89 gold
- HTTPS: 54 alive / 25 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43664
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
