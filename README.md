# SyndProxy private pool

## Current pool

- Alive now: 696
- Gold now: 373
- HTTP: 163 alive / 60 gold
- HTTPS: 113 alive / 17 gold
- SOCKS4: 211 alive / 144 gold
- SOCKS5: 209 alive / 152 gold

## Historical pool

- Discovered: 146656
- Ever alive: 25692
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
