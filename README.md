# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 425
- HTTP: 311 alive / 91 gold
- HTTPS: 226 alive / 21 gold
- SOCKS4: 203 alive / 148 gold
- SOCKS5: 249 alive / 165 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28778
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
