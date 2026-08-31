# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 448
- HTTP: 127 alive / 81 gold
- HTTPS: 90 alive / 35 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45582
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
