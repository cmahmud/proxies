# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 437
- HTTP: 323 alive / 85 gold
- HTTPS: 240 alive / 28 gold
- SOCKS4: 239 alive / 157 gold
- SOCKS5: 264 alive / 167 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32013
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
