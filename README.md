# SyndProxy private pool

## Current pool

- Alive now: 1094
- Gold now: 530
- HTTP: 403 alive / 159 gold
- HTTPS: 278 alive / 93 gold
- SOCKS4: 206 alive / 135 gold
- SOCKS5: 207 alive / 143 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19842
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
