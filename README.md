# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 422
- HTTP: 288 alive / 93 gold
- HTTPS: 213 alive / 23 gold
- SOCKS4: 203 alive / 145 gold
- SOCKS5: 258 alive / 161 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28796
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
