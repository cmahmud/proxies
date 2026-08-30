# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 487
- HTTP: 155 alive / 100 gold
- HTTPS: 131 alive / 46 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 196 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44993
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
