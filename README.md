# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 453
- HTTP: 138 alive / 82 gold
- HTTPS: 108 alive / 35 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 212 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45419
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
