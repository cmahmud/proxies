# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 430
- HTTP: 291 alive / 92 gold
- HTTPS: 203 alive / 25 gold
- SOCKS4: 205 alive / 153 gold
- SOCKS5: 231 alive / 160 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30104
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
