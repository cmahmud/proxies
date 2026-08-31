# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 428
- HTTP: 96 alive / 71 gold
- HTTPS: 59 alive / 26 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45482
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
