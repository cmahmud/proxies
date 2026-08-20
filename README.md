# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 407
- HTTP: 214 alive / 84 gold
- HTTPS: 165 alive / 23 gold
- SOCKS4: 210 alive / 147 gold
- SOCKS5: 262 alive / 153 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27440
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
