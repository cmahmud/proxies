# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 420
- HTTP: 307 alive / 84 gold
- HTTPS: 197 alive / 24 gold
- SOCKS4: 234 alive / 155 gold
- SOCKS5: 235 alive / 157 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30211
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
