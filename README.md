# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 423
- HTTP: 305 alive / 94 gold
- HTTPS: 223 alive / 22 gold
- SOCKS4: 203 alive / 147 gold
- SOCKS5: 251 alive / 160 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28783
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
