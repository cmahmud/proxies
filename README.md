# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 426
- HTTP: 137 alive / 84 gold
- HTTPS: 89 alive / 32 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 196 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44026
- Ever gold: 1390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
