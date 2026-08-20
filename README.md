# SyndProxy private pool

## Current pool

- Alive now: 1742
- Gold now: 647
- HTTP: 670 alive / 210 gold
- HTTPS: 506 alive / 121 gold
- SOCKS4: 230 alive / 154 gold
- SOCKS5: 336 alive / 162 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24191
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
