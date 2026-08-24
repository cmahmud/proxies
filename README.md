# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 402
- HTTP: 108 alive / 69 gold
- HTTPS: 85 alive / 10 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33308
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
