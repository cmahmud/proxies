# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 432
- HTTP: 120 alive / 73 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45533
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
