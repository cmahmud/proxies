# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 425
- HTTP: 135 alive / 85 gold
- HTTPS: 88 alive / 31 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 195 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44029
- Ever gold: 1390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
