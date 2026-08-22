# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 397
- HTTP: 290 alive / 92 gold
- HTTPS: 185 alive / 28 gold
- SOCKS4: 225 alive / 145 gold
- SOCKS5: 214 alive / 132 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31769
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
