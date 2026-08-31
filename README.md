# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 475
- HTTP: 133 alive / 98 gold
- HTTPS: 132 alive / 42 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 197 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45054
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
