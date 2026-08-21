# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 403
- HTTP: 225 alive / 86 gold
- HTTPS: 105 alive / 21 gold
- SOCKS4: 211 alive / 147 gold
- SOCKS5: 230 alive / 149 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29290
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
