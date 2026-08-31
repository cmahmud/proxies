# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 478
- HTTP: 131 alive / 101 gold
- HTTPS: 126 alive / 41 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45057
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
