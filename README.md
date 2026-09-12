# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 417
- HTTP: 108 alive / 74 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 184 alive / 157 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49463
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
