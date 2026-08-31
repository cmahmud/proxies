# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 443
- HTTP: 146 alive / 82 gold
- HTTPS: 113 alive / 29 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 215 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45425
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
