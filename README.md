# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 398
- HTTP: 250 alive / 88 gold
- HTTPS: 153 alive / 24 gold
- SOCKS4: 195 alive / 125 gold
- SOCKS5: 257 alive / 161 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32154
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
