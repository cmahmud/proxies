# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 529
- HTTP: 412 alive / 160 gold
- HTTPS: 235 alive / 82 gold
- SOCKS4: 203 alive / 136 gold
- SOCKS5: 247 alive / 151 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18763
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
