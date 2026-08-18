# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 246
- HTTP: 385 alive / 32 gold
- HTTPS: 189 alive / 6 gold
- SOCKS4: 233 alive / 143 gold
- SOCKS5: 152 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13686
- Ever gold: 428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
