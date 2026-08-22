# SyndProxy private pool

## Current pool

- Alive now: 1231
- Gold now: 371
- HTTP: 487 alive / 83 gold
- HTTPS: 295 alive / 21 gold
- SOCKS4: 171 alive / 104 gold
- SOCKS5: 278 alive / 163 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32470
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
