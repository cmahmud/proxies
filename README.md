# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 390
- HTTP: 195 alive / 79 gold
- HTTPS: 111 alive / 23 gold
- SOCKS4: 231 alive / 143 gold
- SOCKS5: 204 alive / 145 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25253
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
