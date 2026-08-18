# SyndProxy private pool

## Current pool

- Alive now: 671
- Gold now: 247
- HTTP: 174 alive / 30 gold
- HTTPS: 90 alive / 10 gold
- SOCKS4: 221 alive / 118 gold
- SOCKS5: 186 alive / 89 gold

## Historical pool

- Discovered: 86720
- Ever alive: 6881
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
