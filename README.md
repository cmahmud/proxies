# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 398
- HTTP: 79 alive / 57 gold
- HTTPS: 60 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42792
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
