# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 443
- HTTP: 286 alive / 87 gold
- HTTPS: 204 alive / 32 gold
- SOCKS4: 224 alive / 158 gold
- SOCKS5: 268 alive / 166 gold

## Historical pool

- Discovered: 153852
- Ever alive: 28889
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
