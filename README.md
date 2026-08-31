# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 476
- HTTP: 142 alive / 98 gold
- HTTPS: 117 alive / 41 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 201 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45053
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
