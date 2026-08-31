# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 415
- HTTP: 89 alive / 58 gold
- HTTPS: 68 alive / 25 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45499
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
