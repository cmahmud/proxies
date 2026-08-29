# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 366
- HTTP: 95 alive / 50 gold
- HTTPS: 47 alive / 20 gold
- SOCKS4: 156 alive / 149 gold
- SOCKS5: 163 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
