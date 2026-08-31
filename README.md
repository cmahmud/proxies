# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 456
- HTTP: 149 alive / 85 gold
- HTTPS: 105 alive / 36 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 209 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45422
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
