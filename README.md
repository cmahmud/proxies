# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 448
- HTTP: 112 alive / 85 gold
- HTTPS: 62 alive / 31 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 201 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45566
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
