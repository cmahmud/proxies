# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 426
- HTTP: 108 alive / 77 gold
- HTTPS: 55 alive / 22 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 198 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44508
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
