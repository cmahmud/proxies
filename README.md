# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 398
- HTTP: 386 alive / 104 gold
- HTTPS: 265 alive / 24 gold
- SOCKS4: 199 alive / 125 gold
- SOCKS5: 306 alive / 145 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22623
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
