# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 415
- HTTP: 90 alive / 65 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48855
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
