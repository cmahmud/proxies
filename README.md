# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 378
- HTTP: 248 alive / 91 gold
- HTTPS: 174 alive / 26 gold
- SOCKS4: 194 alive / 148 gold
- SOCKS5: 205 alive / 113 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28933
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
