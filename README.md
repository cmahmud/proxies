# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 429
- HTTP: 103 alive / 80 gold
- HTTPS: 66 alive / 22 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44530
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
