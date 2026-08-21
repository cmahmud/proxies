# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 414
- HTTP: 321 alive / 83 gold
- HTTPS: 224 alive / 28 gold
- SOCKS4: 233 alive / 146 gold
- SOCKS5: 236 alive / 157 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30207
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
