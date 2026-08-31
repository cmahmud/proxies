# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 493
- HTTP: 141 alive / 103 gold
- HTTPS: 142 alive / 52 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45009
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
