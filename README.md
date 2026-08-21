# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 427
- HTTP: 346 alive / 114 gold
- HTTPS: 226 alive / 29 gold
- SOCKS4: 233 alive / 140 gold
- SOCKS5: 245 alive / 144 gold

## Historical pool

- Discovered: 160253
- Ever alive: 30683
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
