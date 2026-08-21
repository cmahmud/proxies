# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 391
- HTTP: 251 alive / 90 gold
- HTTPS: 207 alive / 20 gold
- SOCKS4: 183 alive / 138 gold
- SOCKS5: 218 alive / 143 gold

## Historical pool

- Discovered: 152163
- Ever alive: 27860
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
