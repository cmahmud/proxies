# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 418
- HTTP: 95 alive / 62 gold
- HTTPS: 60 alive / 25 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45487
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
