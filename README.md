# SyndProxy private pool

## Current pool

- Alive now: 703
- Gold now: 381
- HTTP: 166 alive / 73 gold
- HTTPS: 122 alive / 20 gold
- SOCKS4: 213 alive / 147 gold
- SOCKS5: 202 alive / 141 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26365
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
