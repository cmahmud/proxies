# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 446
- HTTP: 115 alive / 84 gold
- HTTPS: 70 alive / 29 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45565
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
