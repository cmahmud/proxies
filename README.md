# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 433
- HTTP: 124 alive / 78 gold
- HTTPS: 86 alive / 25 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45459
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
