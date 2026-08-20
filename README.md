# SyndProxy private pool

## Current pool

- Alive now: 648
- Gold now: 351
- HTTP: 157 alive / 69 gold
- HTTPS: 108 alive / 22 gold
- SOCKS4: 189 alive / 122 gold
- SOCKS5: 194 alive / 138 gold

## Historical pool

- Discovered: 145582
- Ever alive: 25585
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
