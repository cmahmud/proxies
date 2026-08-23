# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 341
- HTTP: 141 alive / 37 gold
- HTTPS: 64 alive / 10 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 191 alive / 143 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32837
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
