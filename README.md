# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 420
- HTTP: 219 alive / 85 gold
- HTTPS: 153 alive / 26 gold
- SOCKS4: 209 alive / 150 gold
- SOCKS5: 262 alive / 159 gold

## Historical pool

- Discovered: 153852
- Ever alive: 28891
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
