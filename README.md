# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 262
- HTTP: 239 alive / 30 gold
- HTTPS: 199 alive / 5 gold
- SOCKS4: 217 alive / 118 gold
- SOCKS5: 214 alive / 109 gold

## Historical pool

- Discovered: 99107
- Ever alive: 11854
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
