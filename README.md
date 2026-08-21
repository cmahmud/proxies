# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 398
- HTTP: 258 alive / 88 gold
- HTTPS: 109 alive / 19 gold
- SOCKS4: 224 alive / 139 gold
- SOCKS5: 235 alive / 152 gold

## Historical pool

- Discovered: 157427
- Ever alive: 29752
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
