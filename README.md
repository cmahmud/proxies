# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 520
- HTTP: 323 alive / 157 gold
- HTTPS: 275 alive / 86 gold
- SOCKS4: 203 alive / 141 gold
- SOCKS5: 198 alive / 136 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18452
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
