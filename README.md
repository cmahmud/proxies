# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 492
- HTTP: 146 alive / 102 gold
- HTTPS: 140 alive / 51 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 204 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45001
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
