# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 443
- HTTP: 140 alive / 80 gold
- HTTPS: 107 alive / 29 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 215 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45427
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
