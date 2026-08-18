# SyndProxy private pool

## Current pool

- Alive now: 606
- Gold now: 217
- HTTP: 181 alive / 25 gold
- HTTPS: 77 alive / 7 gold
- SOCKS4: 143 alive / 99 gold
- SOCKS5: 205 alive / 86 gold

## Historical pool

- Discovered: 91696
- Ever alive: 8416
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
