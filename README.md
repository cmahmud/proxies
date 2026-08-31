# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 473
- HTTP: 141 alive / 96 gold
- HTTPS: 126 alive / 41 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 206 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45048
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
