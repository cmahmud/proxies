# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 236
- HTTP: 381 alive / 24 gold
- HTTPS: 176 alive / 9 gold
- SOCKS4: 295 alive / 116 gold
- SOCKS5: 248 alive / 87 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6879
- Ever gold: 321

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
