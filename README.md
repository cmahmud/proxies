# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 469
- HTTP: 158 alive / 102 gold
- HTTPS: 133 alive / 35 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 200 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45156
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
