# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 466
- HTTP: 147 alive / 98 gold
- HTTPS: 130 alive / 37 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45166
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
