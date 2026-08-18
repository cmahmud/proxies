# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 286
- HTTP: 238 alive / 25 gold
- HTTPS: 147 alive / 5 gold
- SOCKS4: 232 alive / 144 gold
- SOCKS5: 225 alive / 112 gold

## Historical pool

- Discovered: 99550
- Ever alive: 12353
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
