# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 424
- HTTP: 106 alive / 77 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44511
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
