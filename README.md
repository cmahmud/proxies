# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 420
- HTTP: 98 alive / 63 gold
- HTTPS: 81 alive / 20 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36059
- Ever gold: 1266

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
