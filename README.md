# SyndProxy private pool

## Current pool

- Alive now: 805
- Gold now: 209
- HTTP: 226 alive / 22 gold
- HTTPS: 168 alive / 7 gold
- SOCKS4: 191 alive / 96 gold
- SOCKS5: 220 alive / 84 gold

## Historical pool

- Discovered: 91696
- Ever alive: 8614
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
