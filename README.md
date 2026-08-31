# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 450
- HTTP: 149 alive / 82 gold
- HTTPS: 99 alive / 34 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 208 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45422
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
