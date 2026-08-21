# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 392
- HTTP: 263 alive / 88 gold
- HTTPS: 107 alive / 26 gold
- SOCKS4: 192 alive / 121 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29467
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
