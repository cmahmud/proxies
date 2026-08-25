# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 415
- HTTP: 103 alive / 63 gold
- HTTPS: 88 alive / 20 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35532
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
