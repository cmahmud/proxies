# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 405
- HTTP: 178 alive / 77 gold
- HTTPS: 147 alive / 22 gold
- SOCKS4: 216 alive / 150 gold
- SOCKS5: 212 alive / 156 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26951
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
