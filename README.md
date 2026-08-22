# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 400
- HTTP: 228 alive / 90 gold
- HTTPS: 184 alive / 32 gold
- SOCKS4: 190 alive / 140 gold
- SOCKS5: 202 alive / 138 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31617
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
