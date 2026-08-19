# SyndProxy private pool

## Current pool

- Alive now: 1321
- Gold now: 526
- HTTP: 521 alive / 181 gold
- HTTPS: 348 alive / 57 gold
- SOCKS4: 207 alive / 124 gold
- SOCKS5: 245 alive / 164 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19664
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
