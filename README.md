# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 353
- HTTP: 307 alive / 50 gold
- HTTPS: 169 alive / 16 gold
- SOCKS4: 238 alive / 147 gold
- SOCKS5: 232 alive / 140 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14805
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
