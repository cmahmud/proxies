# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 412
- HTTP: 102 alive / 66 gold
- HTTPS: 68 alive / 19 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35361
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
