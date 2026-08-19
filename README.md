# SyndProxy private pool

## Current pool

- Alive now: 1197
- Gold now: 528
- HTTP: 439 alive / 183 gold
- HTTPS: 318 alive / 63 gold
- SOCKS4: 199 alive / 123 gold
- SOCKS5: 241 alive / 159 gold

## Historical pool

- Discovered: 125606
- Ever alive: 19590
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
