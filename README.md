# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 422
- HTTP: 106 alive / 78 gold
- HTTPS: 121 alive / 20 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42098
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
