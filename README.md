# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 391
- HTTP: 119 alive / 65 gold
- HTTPS: 54 alive / 13 gold
- SOCKS4: 171 alive / 153 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33185
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
