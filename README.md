# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 390
- HTTP: 238 alive / 92 gold
- HTTPS: 168 alive / 26 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 211 alive / 132 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31605
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
