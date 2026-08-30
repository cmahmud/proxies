# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 429
- HTTP: 136 alive / 87 gold
- HTTPS: 95 alive / 32 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 200 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44025
- Ever gold: 1390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
