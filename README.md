# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 412
- HTTP: 281 alive / 97 gold
- HTTPS: 212 alive / 32 gold
- SOCKS4: 229 alive / 148 gold
- SOCKS5: 243 alive / 135 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30978
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
