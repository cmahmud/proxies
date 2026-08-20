# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 417
- HTTP: 222 alive / 84 gold
- HTTPS: 176 alive / 22 gold
- SOCKS4: 207 alive / 157 gold
- SOCKS5: 220 alive / 154 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27484
- Ever gold: 1098

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
