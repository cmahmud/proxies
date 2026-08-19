# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 521
- HTTP: 437 alive / 157 gold
- HTTPS: 290 alive / 85 gold
- SOCKS4: 200 alive / 143 gold
- SOCKS5: 212 alive / 136 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18508
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
