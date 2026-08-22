# SyndProxy private pool

## Current pool

- Alive now: 805
- Gold now: 382
- HTTP: 227 alive / 86 gold
- HTTPS: 165 alive / 27 gold
- SOCKS4: 197 alive / 123 gold
- SOCKS5: 216 alive / 146 gold

## Historical pool

- Discovered: 163879
- Ever alive: 32033
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
