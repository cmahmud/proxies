# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 415
- HTTP: 95 alive / 65 gold
- HTTPS: 88 alive / 21 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35501
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
