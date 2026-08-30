# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 422
- HTTP: 120 alive / 72 gold
- HTTPS: 68 alive / 22 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44393
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
