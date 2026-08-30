# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 426
- HTTP: 138 alive / 82 gold
- HTTPS: 73 alive / 32 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 265 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43902
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
