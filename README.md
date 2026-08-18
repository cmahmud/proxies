# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 358
- HTTP: 262 alive / 53 gold
- HTTPS: 200 alive / 15 gold
- SOCKS4: 239 alive / 149 gold
- SOCKS5: 245 alive / 141 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14734
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
