# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 407
- HTTP: 275 alive / 88 gold
- HTTPS: 177 alive / 22 gold
- SOCKS4: 203 alive / 137 gold
- SOCKS5: 256 alive / 160 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29043
- Ever gold: 1121

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
