# SyndProxy private pool

## Current pool

- Alive now: 1691
- Gold now: 630
- HTTP: 683 alive / 240 gold
- HTTPS: 522 alive / 127 gold
- SOCKS4: 183 alive / 101 gold
- SOCKS5: 303 alive / 162 gold

## Historical pool

- Discovered: 143105
- Ever alive: 24681
- Ever gold: 1031

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
