# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 448
- HTTP: 150 alive / 84 gold
- HTTPS: 97 alive / 32 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 217 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45445
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
