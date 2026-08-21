# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 386
- HTTP: 186 alive / 82 gold
- HTTPS: 122 alive / 19 gold
- SOCKS4: 217 alive / 136 gold
- SOCKS5: 225 alive / 149 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29763
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
