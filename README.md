# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 415
- HTTP: 91 alive / 61 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45517
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
