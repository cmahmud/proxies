# SyndProxy validated proxy pool

## Current pool

- Alive now: 671
- Gold now: 207
- HTTP: 130 alive / 34 gold
- HTTPS: 140 alive / 7 gold
- SOCKS4: 190 alive / 75 gold
- SOCKS5: 211 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32782
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
