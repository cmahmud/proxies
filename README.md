# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 444
- HTTP: 343 alive / 108 gold
- HTTPS: 252 alive / 28 gold
- SOCKS4: 202 alive / 152 gold
- SOCKS5: 269 alive / 156 gold

## Historical pool

- Discovered: 153725
- Ever alive: 28566
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
