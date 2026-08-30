# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 415
- HTTP: 115 alive / 78 gold
- HTTPS: 54 alive / 28 gold
- SOCKS4: 178 alive / 151 gold
- SOCKS5: 167 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43709
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
