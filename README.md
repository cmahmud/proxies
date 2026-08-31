# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 473
- HTTP: 162 alive / 102 gold
- HTTPS: 123 alive / 37 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45154
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
