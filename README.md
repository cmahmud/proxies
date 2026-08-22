# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 423
- HTTP: 235 alive / 92 gold
- HTTPS: 178 alive / 26 gold
- SOCKS4: 190 alive / 147 gold
- SOCKS5: 230 alive / 158 gold

## Historical pool

- Discovered: 162753
- Ever alive: 31566
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
