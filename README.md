# SyndProxy validated proxy pool

## Current pool

- Alive now: 369
- Gold now: 292
- HTTP: 40 alive / 23 gold
- HTTPS: 7 alive / 0 gold
- SOCKS4: 157 alive / 142 gold
- SOCKS5: 165 alive / 127 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43604
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
