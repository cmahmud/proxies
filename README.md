# SyndProxy private pool

## Current pool

- Alive now: 758
- Gold now: 393
- HTTP: 188 alive / 77 gold
- HTTPS: 154 alive / 28 gold
- SOCKS4: 204 alive / 132 gold
- SOCKS5: 212 alive / 156 gold

## Historical pool

- Discovered: 150519
- Ever alive: 27061
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
