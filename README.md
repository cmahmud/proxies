# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 583
- HTTP: 375 alive / 171 gold
- HTTPS: 307 alive / 142 gold
- SOCKS4: 218 alive / 143 gold
- SOCKS5: 197 alive / 127 gold

## Historical pool

- Discovered: 127405
- Ever alive: 19960
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
