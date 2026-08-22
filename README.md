# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 373
- HTTP: 430 alive / 82 gold
- HTTPS: 272 alive / 22 gold
- SOCKS4: 164 alive / 105 gold
- SOCKS5: 282 alive / 164 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32469
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
