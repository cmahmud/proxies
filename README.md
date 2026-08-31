# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 442
- HTTP: 147 alive / 79 gold
- HTTPS: 98 alive / 30 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 216 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45413
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
