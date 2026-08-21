# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 411
- HTTP: 289 alive / 86 gold
- HTTPS: 186 alive / 21 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 156413
- Ever alive: 29437
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
