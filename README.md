# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 445
- HTTP: 115 alive / 82 gold
- HTTPS: 59 alive / 29 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43693
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
