# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 442
- HTTP: 128 alive / 79 gold
- HTTPS: 118 alive / 34 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44725
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
