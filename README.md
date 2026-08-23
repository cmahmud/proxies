# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 368
- HTTP: 76 alive / 44 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 193 alive / 156 gold
- SOCKS5: 196 alive / 157 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32994
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
