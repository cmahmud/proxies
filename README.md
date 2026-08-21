# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 367
- HTTP: 275 alive / 72 gold
- HTTPS: 179 alive / 23 gold
- SOCKS4: 184 alive / 129 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29669
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
