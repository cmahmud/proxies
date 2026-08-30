# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 450
- HTTP: 139 alive / 92 gold
- HTTPS: 80 alive / 35 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 204 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44178
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
