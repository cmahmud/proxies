# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 342
- HTTP: 282 alive / 67 gold
- HTTPS: 199 alive / 16 gold
- SOCKS4: 186 alive / 111 gold
- SOCKS5: 239 alive / 148 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16118
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
