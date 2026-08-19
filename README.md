# SyndProxy private pool

## Current pool

- Alive now: 1250
- Gold now: 508
- HTTP: 456 alive / 164 gold
- HTTPS: 342 alive / 48 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 233 alive / 149 gold

## Historical pool

- Discovered: 125701
- Ever alive: 19678
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
