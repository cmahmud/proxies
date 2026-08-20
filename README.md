# SyndProxy private pool

## Current pool

- Alive now: 1219
- Gold now: 589
- HTTP: 427 alive / 202 gold
- HTTPS: 317 alive / 101 gold
- SOCKS4: 219 alive / 137 gold
- SOCKS5: 256 alive / 149 gold

## Historical pool

- Discovered: 138948
- Ever alive: 23389
- Ever gold: 919

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
