# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 249
- HTTP: 331 alive / 35 gold
- HTTPS: 186 alive / 8 gold
- SOCKS4: 226 alive / 142 gold
- SOCKS5: 163 alive / 64 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13696
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
