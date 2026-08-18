# SyndProxy private pool

## Current pool

- Alive now: 619
- Gold now: 213
- HTTP: 203 alive / 23 gold
- HTTPS: 76 alive / 7 gold
- SOCKS4: 143 alive / 99 gold
- SOCKS5: 197 alive / 84 gold

## Historical pool

- Discovered: 91696
- Ever alive: 8440
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
