# SyndProxy private pool

## Current pool

- Alive now: 1288
- Gold now: 590
- HTTP: 434 alive / 189 gold
- HTTPS: 295 alive / 100 gold
- SOCKS4: 224 alive / 138 gold
- SOCKS5: 335 alive / 163 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23228
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
