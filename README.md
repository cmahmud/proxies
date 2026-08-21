# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 406
- HTTP: 266 alive / 88 gold
- HTTPS: 184 alive / 22 gold
- SOCKS4: 204 alive / 137 gold
- SOCKS5: 256 alive / 159 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29043
- Ever gold: 1120

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
