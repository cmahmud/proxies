# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 370
- HTTP: 203 alive / 66 gold
- HTTPS: 119 alive / 13 gold
- SOCKS4: 184 alive / 145 gold
- SOCKS5: 205 alive / 146 gold

## Historical pool

- Discovered: 146589
- Ever alive: 25658
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
