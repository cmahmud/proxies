# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 448
- HTTP: 346 alive / 100 gold
- HTTPS: 242 alive / 31 gold
- SOCKS4: 212 alive / 147 gold
- SOCKS5: 261 alive / 170 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28716
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
