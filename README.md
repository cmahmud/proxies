# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 399
- HTTP: 194 alive / 87 gold
- HTTPS: 118 alive / 22 gold
- SOCKS4: 202 alive / 146 gold
- SOCKS5: 235 alive / 144 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29139
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
