# SyndProxy private pool

## Current pool

- Alive now: 1256
- Gold now: 437
- HTTP: 440 alive / 100 gold
- HTTPS: 277 alive / 24 gold
- SOCKS4: 223 alive / 150 gold
- SOCKS5: 316 alive / 163 gold

## Historical pool

- Discovered: 136246
- Ever alive: 22636
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
