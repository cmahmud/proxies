# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 278
- HTTP: 294 alive / 40 gold
- HTTPS: 191 alive / 8 gold
- SOCKS4: 220 alive / 138 gold
- SOCKS5: 164 alive / 92 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13778
- Ever gold: 430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
