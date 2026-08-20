# SyndProxy private pool

## Current pool

- Alive now: 797
- Gold now: 406
- HTTP: 191 alive / 78 gold
- HTTPS: 154 alive / 23 gold
- SOCKS4: 228 alive / 154 gold
- SOCKS5: 224 alive / 151 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26625
- Ever gold: 1084

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
