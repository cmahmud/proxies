# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 441
- HTTP: 150 alive / 79 gold
- HTTPS: 99 alive / 30 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 211 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45409
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
