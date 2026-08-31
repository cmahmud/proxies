# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 467
- HTTP: 157 alive / 92 gold
- HTTPS: 134 alive / 38 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 233 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45273
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
