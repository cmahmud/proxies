# SyndProxy private pool

## Current pool

- Alive now: 1928
- Gold now: 644
- HTTP: 752 alive / 231 gold
- HTTPS: 599 alive / 101 gold
- SOCKS4: 255 alive / 148 gold
- SOCKS5: 322 alive / 164 gold

## Historical pool

- Discovered: 142698
- Ever alive: 24336
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
