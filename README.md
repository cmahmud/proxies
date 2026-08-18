# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 258
- HTTP: 302 alive / 29 gold
- HTTPS: 182 alive / 5 gold
- SOCKS4: 197 alive / 116 gold
- SOCKS5: 221 alive / 108 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11821
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
