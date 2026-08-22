# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 420
- HTTP: 326 alive / 92 gold
- HTTPS: 243 alive / 27 gold
- SOCKS4: 220 alive / 143 gold
- SOCKS5: 243 alive / 158 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32084
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
