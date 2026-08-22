# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 336
- HTTP: 343 alive / 82 gold
- HTTPS: 213 alive / 21 gold
- SOCKS4: 197 alive / 142 gold
- SOCKS5: 203 alive / 91 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32498
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
