# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 398
- HTTP: 213 alive / 96 gold
- HTTPS: 216 alive / 27 gold
- SOCKS4: 191 alive / 126 gold
- SOCKS5: 214 alive / 149 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31378
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
