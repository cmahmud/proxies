# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 422
- HTTP: 115 alive / 69 gold
- HTTPS: 78 alive / 22 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45522
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
