# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 403
- HTTP: 185 alive / 85 gold
- HTTPS: 152 alive / 23 gold
- SOCKS4: 196 alive / 144 gold
- SOCKS5: 233 alive / 151 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27422
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
