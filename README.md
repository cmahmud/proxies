# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 448
- HTTP: 146 alive / 82 gold
- HTTPS: 102 alive / 32 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 222 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45445
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
