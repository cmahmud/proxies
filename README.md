# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 429
- HTTP: 106 alive / 79 gold
- HTTPS: 46 alive / 22 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44520
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
