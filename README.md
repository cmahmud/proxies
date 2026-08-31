# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 448
- HTTP: 126 alive / 82 gold
- HTTPS: 88 alive / 34 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45582
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
