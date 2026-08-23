# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 260
- HTTP: 131 alive / 36 gold
- HTTPS: 53 alive / 4 gold
- SOCKS4: 167 alive / 90 gold
- SOCKS5: 181 alive / 130 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32786
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
