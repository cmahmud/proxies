# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 482
- HTTP: 140 alive / 102 gold
- HTTPS: 124 alive / 44 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45071
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
