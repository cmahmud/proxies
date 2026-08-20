# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 384
- HTTP: 169 alive / 64 gold
- HTTPS: 113 alive / 20 gold
- SOCKS4: 210 alive / 145 gold
- SOCKS5: 210 alive / 155 gold

## Historical pool

- Discovered: 146656
- Ever alive: 25692
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
