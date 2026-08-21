# SyndProxy private pool

## Current pool

- Alive now: 784
- Gold now: 402
- HTTP: 231 alive / 89 gold
- HTTPS: 145 alive / 20 gold
- SOCKS4: 196 alive / 136 gold
- SOCKS5: 212 alive / 157 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27623
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
