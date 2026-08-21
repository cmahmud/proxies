# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 385
- HTTP: 256 alive / 68 gold
- HTTPS: 180 alive / 23 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 221 alive / 153 gold

## Historical pool

- Discovered: 157410
- Ever alive: 29681
- Ever gold: 1136

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
