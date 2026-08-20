# SyndProxy private pool

## Current pool

- Alive now: 714
- Gold now: 359
- HTTP: 175 alive / 57 gold
- HTTPS: 115 alive / 17 gold
- SOCKS4: 200 alive / 143 gold
- SOCKS5: 224 alive / 142 gold

## Historical pool

- Discovered: 147647
- Ever alive: 25865
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
