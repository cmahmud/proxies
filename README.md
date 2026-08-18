# SyndProxy private pool

## Current pool

- Alive now: 661
- Gold now: 248
- HTTP: 160 alive / 34 gold
- HTTPS: 87 alive / 7 gold
- SOCKS4: 211 alive / 123 gold
- SOCKS5: 203 alive / 84 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9352
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
