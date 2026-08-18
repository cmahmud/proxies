# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 274
- HTTP: 328 alive / 37 gold
- HTTPS: 186 alive / 8 gold
- SOCKS4: 213 alive / 137 gold
- SOCKS5: 163 alive / 92 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13932
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
