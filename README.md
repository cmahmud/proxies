# SyndProxy private pool

## Current pool

- Alive now: 1167
- Gold now: 410
- HTTP: 469 alive / 91 gold
- HTTPS: 263 alive / 32 gold
- SOCKS4: 200 alive / 128 gold
- SOCKS5: 235 alive / 159 gold

## Historical pool

- Discovered: 163242
- Ever alive: 31699
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
