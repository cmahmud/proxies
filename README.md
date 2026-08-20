# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 380
- HTTP: 183 alive / 78 gold
- HTTPS: 142 alive / 19 gold
- SOCKS4: 218 alive / 143 gold
- SOCKS5: 202 alive / 140 gold

## Historical pool

- Discovered: 149511
- Ever alive: 26899
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
