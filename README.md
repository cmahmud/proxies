# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 475
- HTTP: 145 alive / 102 gold
- HTTPS: 104 alive / 37 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45125
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
