# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 410
- HTTP: 289 alive / 89 gold
- HTTPS: 164 alive / 23 gold
- SOCKS4: 221 alive / 141 gold
- SOCKS5: 242 alive / 157 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31967
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
