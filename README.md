# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 368
- HTTP: 297 alive / 88 gold
- HTTPS: 197 alive / 18 gold
- SOCKS4: 214 alive / 141 gold
- SOCKS5: 211 alive / 121 gold

## Historical pool

- Discovered: 119839
- Ever alive: 18361
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
