# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 387
- HTTP: 173 alive / 69 gold
- HTTPS: 137 alive / 20 gold
- SOCKS4: 203 alive / 142 gold
- SOCKS5: 230 alive / 156 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25561
- Ever gold: 1065

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
