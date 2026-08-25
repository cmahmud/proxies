# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 414
- HTTP: 105 alive / 70 gold
- HTTPS: 83 alive / 22 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34982
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
