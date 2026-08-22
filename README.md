# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 335
- HTTP: 333 alive / 80 gold
- HTTPS: 226 alive / 21 gold
- SOCKS4: 198 alive / 142 gold
- SOCKS5: 202 alive / 92 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32498
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
