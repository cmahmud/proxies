# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 440
- HTTP: 358 alive / 111 gold
- HTTPS: 252 alive / 33 gold
- SOCKS4: 200 alive / 154 gold
- SOCKS5: 249 alive / 142 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28645
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
