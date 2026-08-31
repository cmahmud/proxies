# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 483
- HTTP: 151 alive / 105 gold
- HTTPS: 135 alive / 39 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 194 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45226
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
