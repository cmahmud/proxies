# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 431
- HTTP: 113 alive / 86 gold
- HTTPS: 45 alive / 29 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49428
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
