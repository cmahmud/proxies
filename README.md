# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 473
- HTTP: 149 alive / 100 gold
- HTTPS: 134 alive / 37 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45146
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
