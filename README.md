# SyndProxy private pool

## Current pool

- Alive now: 662
- Gold now: 353
- HTTP: 168 alive / 69 gold
- HTTPS: 118 alive / 23 gold
- SOCKS4: 185 alive / 124 gold
- SOCKS5: 191 alive / 137 gold

## Historical pool

- Discovered: 145581
- Ever alive: 25582
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
