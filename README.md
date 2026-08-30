# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 442
- HTTP: 109 alive / 81 gold
- HTTPS: 50 alive / 28 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43686
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
