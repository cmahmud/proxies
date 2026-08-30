# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 427
- HTTP: 113 alive / 76 gold
- HTTPS: 51 alive / 23 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44523
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
