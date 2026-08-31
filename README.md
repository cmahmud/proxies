# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 482
- HTTP: 139 alive / 101 gold
- HTTPS: 114 alive / 45 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 202 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45066
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
