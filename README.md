# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 257
- HTTP: 130 alive / 37 gold
- HTTPS: 67 alive / 5 gold
- SOCKS4: 167 alive / 89 gold
- SOCKS5: 181 alive / 126 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32785
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
