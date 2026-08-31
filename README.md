# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 472
- HTTP: 141 alive / 95 gold
- HTTPS: 119 alive / 41 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 202 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45048
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
