# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 444
- HTTP: 332 alive / 86 gold
- HTTPS: 238 alive / 30 gold
- SOCKS4: 241 alive / 157 gold
- SOCKS5: 265 alive / 171 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32015
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
