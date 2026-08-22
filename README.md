# SyndProxy private pool

## Current pool

- Alive now: 948
- Gold now: 398
- HTTP: 296 alive / 91 gold
- HTTPS: 182 alive / 20 gold
- SOCKS4: 203 alive / 124 gold
- SOCKS5: 267 alive / 163 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32151
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
