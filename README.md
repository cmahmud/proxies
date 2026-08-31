# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 442
- HTTP: 118 alive / 78 gold
- HTTPS: 92 alive / 30 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45451
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
