# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 457
- HTTP: 128 alive / 90 gold
- HTTPS: 119 alive / 35 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44803
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
