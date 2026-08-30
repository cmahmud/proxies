# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 445
- HTTP: 135 alive / 83 gold
- HTTPS: 65 alive / 29 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43695
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
