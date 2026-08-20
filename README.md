# SyndProxy private pool

## Current pool

- Alive now: 1702
- Gold now: 646
- HTTP: 668 alive / 213 gold
- HTTPS: 478 alive / 121 gold
- SOCKS4: 221 alive / 151 gold
- SOCKS5: 335 alive / 161 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24191
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
