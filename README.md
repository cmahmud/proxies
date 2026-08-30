# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 434
- HTTP: 114 alive / 81 gold
- HTTPS: 54 alive / 25 gold
- SOCKS4: 164 alive / 161 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44523
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
