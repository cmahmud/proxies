# SyndProxy private pool

## Current pool

- Alive now: 1776
- Gold now: 641
- HTTP: 714 alive / 219 gold
- HTTPS: 511 alive / 116 gold
- SOCKS4: 215 alive / 147 gold
- SOCKS5: 336 alive / 159 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24201
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
