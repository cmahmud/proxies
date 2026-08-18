# SyndProxy private pool

## Current pool

- Alive now: 652
- Gold now: 243
- HTTP: 166 alive / 28 gold
- HTTPS: 94 alive / 9 gold
- SOCKS4: 205 alive / 119 gold
- SOCKS5: 187 alive / 87 gold

## Historical pool

- Discovered: 86739
- Ever alive: 6883
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
