# SyndProxy private pool

## Current pool

- Alive now: 1297
- Gold now: 507
- HTTP: 487 alive / 163 gold
- HTTPS: 353 alive / 48 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 237 alive / 149 gold

## Historical pool

- Discovered: 125701
- Ever alive: 19678
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
