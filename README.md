# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 443
- HTTP: 135 alive / 82 gold
- HTTPS: 66 alive / 29 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43695
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
