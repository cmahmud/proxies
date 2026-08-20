# SyndProxy private pool

## Current pool

- Alive now: 1583
- Gold now: 590
- HTTP: 646 alive / 189 gold
- HTTPS: 422 alive / 92 gold
- SOCKS4: 247 alive / 142 gold
- SOCKS5: 268 alive / 167 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23157
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
