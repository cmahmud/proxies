# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 471
- HTTP: 146 alive / 98 gold
- HTTPS: 116 alive / 35 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45129
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
