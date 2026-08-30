# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 423
- HTTP: 130 alive / 85 gold
- HTTPS: 91 alive / 29 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 193 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44035
- Ever gold: 1390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
