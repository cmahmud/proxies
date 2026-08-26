# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 379
- HTTP: 119 alive / 66 gold
- HTTPS: 170 alive / 17 gold
- SOCKS4: 158 alive / 147 gold
- SOCKS5: 170 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40095
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
