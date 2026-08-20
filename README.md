# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 378
- HTTP: 189 alive / 79 gold
- HTTPS: 150 alive / 22 gold
- SOCKS4: 226 alive / 144 gold
- SOCKS5: 211 alive / 133 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26624
- Ever gold: 1084

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
