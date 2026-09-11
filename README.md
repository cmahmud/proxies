# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 415
- HTTP: 91 alive / 66 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48854
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
