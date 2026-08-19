# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 534
- HTTP: 352 alive / 153 gold
- HTTPS: 231 alive / 88 gold
- SOCKS4: 212 alive / 150 gold
- SOCKS5: 212 alive / 143 gold

## Historical pool

- Discovered: 119811
- Ever alive: 18038
- Ever gold: 712

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
