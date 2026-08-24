# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 381
- HTTP: 105 alive / 48 gold
- HTTPS: 35 alive / 11 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33536
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
