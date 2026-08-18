# SyndProxy private pool

## Current pool

- Alive now: 602
- Gold now: 226
- HTTP: 163 alive / 25 gold
- HTTPS: 77 alive / 7 gold
- SOCKS4: 160 alive / 112 gold
- SOCKS5: 202 alive / 82 gold

## Historical pool

- Discovered: 91696
- Ever alive: 8401
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
