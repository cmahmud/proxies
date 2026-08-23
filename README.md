# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 341
- HTTP: 100 alive / 37 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 176 alive / 151 gold
- SOCKS5: 171 alive / 143 gold

## Historical pool

- Discovered: 171050
- Ever alive: 32856
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
