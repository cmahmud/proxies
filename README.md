# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 390
- HTTP: 335 alive / 91 gold
- HTTPS: 187 alive / 15 gold
- SOCKS4: 229 alive / 156 gold
- SOCKS5: 207 alive / 128 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18236
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
