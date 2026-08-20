# SyndProxy private pool

## Current pool

- Alive now: 805
- Gold now: 385
- HTTP: 204 alive / 73 gold
- HTTPS: 186 alive / 16 gold
- SOCKS4: 207 alive / 149 gold
- SOCKS5: 208 alive / 147 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26487
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
