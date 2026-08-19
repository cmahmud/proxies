# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 365
- HTTP: 305 alive / 68 gold
- HTTPS: 231 alive / 18 gold
- SOCKS4: 256 alive / 157 gold
- SOCKS5: 218 alive / 122 gold

## Historical pool

- Discovered: 110860
- Ever alive: 15961
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
