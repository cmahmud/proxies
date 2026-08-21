# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 434
- HTTP: 328 alive / 99 gold
- HTTPS: 229 alive / 28 gold
- SOCKS4: 198 alive / 144 gold
- SOCKS5: 262 alive / 163 gold

## Historical pool

- Discovered: 153744
- Ever alive: 28756
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
