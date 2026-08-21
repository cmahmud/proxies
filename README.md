# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 399
- HTTP: 326 alive / 84 gold
- HTTPS: 188 alive / 24 gold
- SOCKS4: 207 alive / 129 gold
- SOCKS5: 257 alive / 162 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29711
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
