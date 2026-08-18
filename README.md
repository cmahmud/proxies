# SyndProxy private pool

## Current pool

- Alive now: 626
- Gold now: 208
- HTTP: 146 alive / 24 gold
- HTTPS: 78 alive / 9 gold
- SOCKS4: 189 alive / 93 gold
- SOCKS5: 213 alive / 82 gold

## Historical pool

- Discovered: 91002
- Ever alive: 8003
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
