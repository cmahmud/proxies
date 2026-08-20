# SyndProxy private pool

## Current pool

- Alive now: 1789
- Gold now: 706
- HTTP: 650 alive / 240 gold
- HTTPS: 559 alive / 146 gold
- SOCKS4: 244 alive / 157 gold
- SOCKS5: 336 alive / 163 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24395
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
