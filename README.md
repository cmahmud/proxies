# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 421
- HTTP: 99 alive / 63 gold
- HTTPS: 80 alive / 21 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36059
- Ever gold: 1266

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
