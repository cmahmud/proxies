# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 415
- HTTP: 106 alive / 60 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45517
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
