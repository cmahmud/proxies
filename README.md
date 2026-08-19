# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 506
- HTTP: 403 alive / 147 gold
- HTTPS: 269 alive / 87 gold
- SOCKS4: 194 alive / 117 gold
- SOCKS5: 237 alive / 155 gold

## Historical pool

- Discovered: 119650
- Ever alive: 17830
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
