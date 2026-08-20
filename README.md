# SyndProxy private pool

## Current pool

- Alive now: 1582
- Gold now: 613
- HTTP: 617 alive / 219 gold
- HTTPS: 507 alive / 115 gold
- SOCKS4: 210 alive / 136 gold
- SOCKS5: 248 alive / 143 gold

## Historical pool

- Discovered: 141135
- Ever alive: 23838
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
