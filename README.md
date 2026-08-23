# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 221
- HTTP: 141 alive / 37 gold
- HTTPS: 76 alive / 6 gold
- SOCKS4: 167 alive / 88 gold
- SOCKS5: 182 alive / 90 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32783
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
