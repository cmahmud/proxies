# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 424
- HTTP: 289 alive / 82 gold
- HTTPS: 200 alive / 24 gold
- SOCKS4: 238 alive / 152 gold
- SOCKS5: 252 alive / 166 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32011
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
