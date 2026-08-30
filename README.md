# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 488
- HTTP: 148 alive / 100 gold
- HTTPS: 125 alive / 46 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 199 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44994
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
