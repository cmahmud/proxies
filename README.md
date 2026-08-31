# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 470
- HTTP: 148 alive / 95 gold
- HTTPS: 113 alive / 36 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 204 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45108
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
