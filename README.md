# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 365
- HTTP: 336 alive / 91 gold
- HTTPS: 163 alive / 29 gold
- SOCKS4: 166 alive / 104 gold
- SOCKS5: 241 alive / 141 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32568
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
