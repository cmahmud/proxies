# SyndProxy private pool

## Current pool

- Alive now: 788
- Gold now: 364
- HTTP: 191 alive / 70 gold
- HTTPS: 149 alive / 22 gold
- SOCKS4: 223 alive / 147 gold
- SOCKS5: 225 alive / 125 gold

## Historical pool

- Discovered: 145547
- Ever alive: 25389
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
