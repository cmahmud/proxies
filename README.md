# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 415
- HTTP: 117 alive / 68 gold
- HTTPS: 90 alive / 19 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35392
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
