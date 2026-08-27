# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 418
- HTTP: 98 alive / 76 gold
- HTTPS: 78 alive / 20 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41764
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
