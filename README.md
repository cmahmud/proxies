# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 442
- HTTP: 131 alive / 89 gold
- HTTPS: 55 alive / 26 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43664
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
