# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 423
- HTTP: 110 alive / 68 gold
- HTTPS: 68 alive / 24 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44410
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
