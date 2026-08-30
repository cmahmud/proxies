# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 463
- HTTP: 121 alive / 91 gold
- HTTPS: 118 alive / 36 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 204 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44892
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
