# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 381
- HTTP: 233 alive / 86 gold
- HTTPS: 186 alive / 26 gold
- SOCKS4: 198 alive / 122 gold
- SOCKS5: 232 alive / 147 gold

## Historical pool

- Discovered: 164184
- Ever alive: 32058
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
