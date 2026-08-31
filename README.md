# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 470
- HTTP: 156 alive / 102 gold
- HTTPS: 136 alive / 35 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45156
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
