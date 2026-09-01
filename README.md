# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 452
- HTTP: 129 alive / 89 gold
- HTTPS: 132 alive / 29 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 214 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46589
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
