# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 423
- HTTP: 104 alive / 66 gold
- HTTPS: 110 alive / 25 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35667
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
