# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 433
- HTTP: 120 alive / 78 gold
- HTTPS: 91 alive / 24 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 199 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45459
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
