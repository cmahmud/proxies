# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 357
- HTTP: 98 alive / 37 gold
- HTTPS: 42 alive / 9 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 181 alive / 156 gold

## Historical pool

- Discovered: 171599
- Ever alive: 32939
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
