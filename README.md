# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 427
- HTTP: 289 alive / 82 gold
- HTTPS: 198 alive / 24 gold
- SOCKS4: 239 alive / 155 gold
- SOCKS5: 253 alive / 166 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32012
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
