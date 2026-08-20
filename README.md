# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 385
- HTTP: 190 alive / 78 gold
- HTTPS: 166 alive / 23 gold
- SOCKS4: 211 alive / 125 gold
- SOCKS5: 228 alive / 159 gold

## Historical pool

- Discovered: 150719
- Ever alive: 27074
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
