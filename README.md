# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 473
- HTTP: 135 alive / 95 gold
- HTTPS: 122 alive / 38 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 201 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44890
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
