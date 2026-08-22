# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 418
- HTTP: 323 alive / 89 gold
- HTTPS: 203 alive / 26 gold
- SOCKS4: 203 alive / 144 gold
- SOCKS5: 249 alive / 159 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31556
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
