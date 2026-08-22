# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 387
- HTTP: 241 alive / 97 gold
- HTTPS: 159 alive / 27 gold
- SOCKS4: 198 alive / 135 gold
- SOCKS5: 197 alive / 128 gold

## Historical pool

- Discovered: 162755
- Ever alive: 31579
- Ever gold: 1162

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
