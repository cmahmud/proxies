# SyndProxy private pool

## Current pool

- Alive now: 1378
- Gold now: 407
- HTTP: 480 alive / 77 gold
- HTTPS: 340 alive / 16 gold
- SOCKS4: 247 alive / 156 gold
- SOCKS5: 311 alive / 158 gold

## Historical pool

- Discovered: 134532
- Ever alive: 21948
- Ever gold: 889

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
