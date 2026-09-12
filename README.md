# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 464
- HTTP: 134 alive / 100 gold
- HTTPS: 58 alive / 33 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49330
- Ever gold: 1577

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
