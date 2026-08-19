# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 341
- HTTP: 275 alive / 68 gold
- HTTPS: 183 alive / 17 gold
- SOCKS4: 190 alive / 112 gold
- SOCKS5: 221 alive / 144 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16155
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
