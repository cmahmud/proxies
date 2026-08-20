# SyndProxy private pool

## Current pool

- Alive now: 1943
- Gold now: 694
- HTTP: 784 alive / 232 gold
- HTTPS: 601 alive / 147 gold
- SOCKS4: 228 alive / 149 gold
- SOCKS5: 330 alive / 166 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24464
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
