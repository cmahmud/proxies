# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 560
- HTTP: 402 alive / 170 gold
- HTTPS: 288 alive / 133 gold
- SOCKS4: 193 alive / 124 gold
- SOCKS5: 193 alive / 133 gold

## Historical pool

- Discovered: 127417
- Ever alive: 19966
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
