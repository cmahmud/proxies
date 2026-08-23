# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 347
- HTTP: 129 alive / 40 gold
- HTTPS: 101 alive / 8 gold
- SOCKS4: 182 alive / 154 gold
- SOCKS5: 207 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
